import bpy
from bpy.types import Operator


def fetch_user_preferences(attr_id=None):
    prefs = bpy.context.preferences.addons[__package__].preferences

    if attr_id is None:
        return prefs
    else:
        return getattr(prefs, attr_id)


class ImprovedDuplicateBaseclass:
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        space = context.space_data
        is_existing = space.node_tree is not None
        is_node_editor = space.type == "NODE_EDITOR"
        return all((is_existing, is_node_editor))

    def execute(self, context):
        if not self.filter_frames:
            selected_nodes = context.selected_nodes
            if not selected_nodes:
                return {"CANCELLED"}

            bpy.ops.node.duplicate(keep_inputs=self.keep_inputs, linked=self.linked)

        else:
            selected_nodes = [
                node for node in context.selected_nodes if node.bl_idname != "NodeFrame"
            ]

            if not selected_nodes:
                return {"CANCELLED"}

            for node in context.selected_nodes:
                if node.bl_idname == "NodeFrame":
                    node.select = False

            bpy.ops.node.duplicate(keep_inputs=self.keep_inputs, linked=self.linked)

            for node in context.selected_nodes:
                node.parent = None

        if fetch_user_preferences(attr_id="remove_on_cancel"):
            bpy.ops.node.translate_attach_remove_on_cancel("INVOKE_DEFAULT")
        else:
            bpy.ops.node.translate_attach("INVOKE_DEFAULT")

        return {"FINISHED"}


class NODE_OT_IMPROVED_DUPLICATE(Operator, ImprovedDuplicateBaseclass):
    bl_label = "Duplicate"
    bl_idname = "node.improved_duplicate"
    bl_description = "Make a copy of currently selected nodes"

    filter_frames = False
    keep_inputs = False
    linked = False


class NODE_OT_IMPROVED_DUPLICATE_LINKED(Operator, ImprovedDuplicateBaseclass):
    bl_label = "Duplicate (Linked)"
    bl_idname = "node.improved_duplicate_linked"
    bl_description = "Make a copy of currently selected nodes but not their node trees"

    filter_frames = False
    keep_inputs = False
    linked = True


class NODE_OT_IMPROVED_DUPLICATE_KEEP_INPUTS(Operator, ImprovedDuplicateBaseclass):
    bl_label = "Duplicate (Keep Inputs)"
    bl_idname = "node.improved_duplicate_keep_inputs"
    bl_description = (
        "Make a copy of currently selected nodes while preserving existing input links"
    )

    filter_frames = False
    keep_inputs = True
    linked = False


class NODE_OT_IMPROVED_DUPLICATE_LINKED_KEEP_INPUTS(
    Operator, ImprovedDuplicateBaseclass
):
    bl_label = "Duplicate (Linked & Keep Inputs)"
    bl_idname = "node.improved_duplicate_linked_keep_inputs"
    bl_description = "Make a copy of currently selected nodes but not their node trees, while preserving existing input links"

    filter_frames = False
    keep_inputs = True
    linked = True


class NODE_OT_IMPROVED_DUPLICATE_UNFRAMED(Operator, ImprovedDuplicateBaseclass):
    bl_label = "Duplicate Unframed"
    bl_idname = "node.improved_duplicate_unframed"
    bl_description = "Make a copy of currently selected nodes (excluding frames)"

    filter_frames = True
    keep_inputs = False
    linked = False


class NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_LINKED(Operator, ImprovedDuplicateBaseclass):
    bl_label = "Duplicate Unframed (Linked)"
    bl_idname = "node.improved_duplicate_unframed_linked"
    bl_description = "Make a copy of currently selected nodes (excluding frames), but not their node trees"

    filter_frames = True
    keep_inputs = False
    linked = True


class NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_KEEP_INPUTS(
    Operator, ImprovedDuplicateBaseclass
):
    bl_label = "Duplicate Unframed (Keep Inputs)"
    bl_idname = "node.improved_duplicate_unframed_keep_inputs"
    bl_description = "Make a copy of currently selected nodes (excluding frames), while preserving existing input links"

    filter_frames = True
    keep_inputs = True
    linked = False


class NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_LINKED_KEEP_INPUTS(
    Operator, ImprovedDuplicateBaseclass
):
    bl_label = "Duplicate Unframed (Linked & Keep Inputs)"
    bl_idname = "node.improved_duplicate_unframed_linked_keep_inputs"
    bl_description = "Make a copy of currently selected nodes but not their node trees (excluding frames), while preserving existing input links"

    filter_frames = True
    keep_inputs = True
    linked = True


classes = (
    NODE_OT_IMPROVED_DUPLICATE,
    NODE_OT_IMPROVED_DUPLICATE_LINKED,
    NODE_OT_IMPROVED_DUPLICATE_KEEP_INPUTS,
    NODE_OT_IMPROVED_DUPLICATE_LINKED_KEEP_INPUTS,
    NODE_OT_IMPROVED_DUPLICATE_UNFRAMED,
    NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_LINKED,
    NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_KEEP_INPUTS,
    NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_LINKED_KEEP_INPUTS,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
