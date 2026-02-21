import os, bpy
from bpy.props import *
from bpy_extras.io_utils import ImportHelper

# ################################################################
# Import/Export
# ################################################################
class ImportCmb(bpy.types.Operator, ImportHelper):
    bl_idname = "import.cmb"
    bl_label = "Import CMB"
    
    filename_ext = ".cmb"
    filter_glob = StringProperty(default="*.cmb", options={'HIDDEN'})
    files = bpy.props.CollectionProperty(type=bpy.types.OperatorFileListElement, options={'HIDDEN', 'SKIP_SAVE'})
    directory = bpy.props.StringProperty(subtype='FILE_PATH', options={'HIDDEN', 'SKIP_SAVE'})
    
    
    def execute( self, context ):
        from .import_cmb import load_cmb
        return load_cmb(self, context)


# ################################################################
# Common
# ################################################################

def menu_func_import( self, context ):
    self.layout.operator( ImportCmb.bl_idname, text="CtrModelBinary (.cmb)")

def register():
    print("Registering CMB\n")
    bpy.utils.register_class(ImportCmb)
    bpy.types.INFO_MT_file_import.append(menu_func_import)
    
def unregister():
    print("Unregistering CMB\n")
    bpy.utils.unregister_class(ImportCmb)
    bpy.types.INFO_MT_file_import.remove(menu_func_import)
    
if __name__ == "__main__":
    register()
