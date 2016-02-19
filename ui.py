import bpy


class CustomPropsEditPanel(bpy.types.Panel):
    bl_idname = "custom_props_edit_panel"
    bl_label = "Remove Custom Properties"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align = True)
        row.operator("cpe.search_custom_properties", text = "Search", icon = "VIEWZOOM")
        row.operator("cpe.remove_selected_properties", text = "Remove", icon = "X")
        
        settings = context.scene.custom_props_edit
        
        box = layout.box()
        header_row = box.row(align = True)
        header_row.label("Name")
        header_row.prop(settings, "remove_all")
        
        col = box.column(align = True)
        for item in settings.property_edit_settings:
            row = col.row(align = True)
            row.label(repr(item.property_name))
            row.prop(item, "remove")
            
        