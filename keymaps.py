from .keymap_ui import KeymapItemDef, KeymapStructure, KeymapLayout
from .operators import (
    NODE_OT_IMPROVED_DUPLICATE,
    NODE_OT_IMPROVED_DUPLICATE_LINKED,
    NODE_OT_IMPROVED_DUPLICATE_KEEP_INPUTS,
    NODE_OT_IMPROVED_DUPLICATE_LINKED_KEEP_INPUTS,
    NODE_OT_IMPROVED_DUPLICATE_UNFRAMED,
    NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_LINKED,
    NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_KEEP_INPUTS,
    NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_LINKED_KEEP_INPUTS,
)


keymap_info = {
    "keymap_name": "Node Editor",
    "space_type": "NODE_EDITOR",
}


keymap_structure = KeymapStructure(
    {
        "Duplicate Nodes": (
            KeymapItemDef(NODE_OT_IMPROVED_DUPLICATE.bl_idname, **keymap_info),
            KeymapItemDef(NODE_OT_IMPROVED_DUPLICATE_LINKED.bl_idname, **keymap_info),
            KeymapItemDef(
                NODE_OT_IMPROVED_DUPLICATE_KEEP_INPUTS.bl_idname, **keymap_info
            ),
            KeymapItemDef(
                NODE_OT_IMPROVED_DUPLICATE_LINKED_KEEP_INPUTS.bl_idname, **keymap_info
            ),
        ),
        "Duplicate Nodes (Unframed)": (
            KeymapItemDef(NODE_OT_IMPROVED_DUPLICATE_UNFRAMED.bl_idname, **keymap_info),
            KeymapItemDef(
                NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_LINKED.bl_idname, **keymap_info
            ),
            KeymapItemDef(
                NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_KEEP_INPUTS.bl_idname, **keymap_info
            ),
            KeymapItemDef(
                NODE_OT_IMPROVED_DUPLICATE_UNFRAMED_LINKED_KEEP_INPUTS.bl_idname,
                **keymap_info,
            ),
        ),
    }
)


keymap_layout = KeymapLayout(layout_structure=keymap_structure)


def register():
    keymap_structure.register()


def unregister():
    keymap_structure.unregister()
