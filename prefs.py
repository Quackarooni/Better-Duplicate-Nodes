import bpy
from bpy.props import BoolProperty
from copy import copy

from .operators import fetch_user_preferences
from .keymaps import keymap_layout


user_edit_prefs = bpy.context.preferences.edit
old_pref_value = None


class DuplicateNodesPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    remove_on_cancel: BoolProperty(
        name="Remove Nodes on Cancel",
        default=True,
        description="When the operator is cancelled, remove duplicated nodes",
    )

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, "remove_on_cancel")
        row.prop(
            context.preferences.edit,
            "use_duplicate_node_tree",
            text="Link Groups by Default",
            invert_checkbox=True,
        )

        keymap_layout.draw_keyboard_shorcuts(self, layout, context)


keymap_layout.register_properties(preferences=DuplicateNodesPreferences)


classes = (DuplicateNodesPreferences,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    global old_pref_value
    old_pref_value = copy(user_edit_prefs.use_duplicate_node_tree)
    user_edit_prefs.use_duplicate_node_tree = False

    prefs = fetch_user_preferences()
    prefs.property_unset("show_keymaps")


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    user_edit_prefs.use_duplicate_node_tree = old_pref_value
