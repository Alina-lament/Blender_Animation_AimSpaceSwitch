import bpy

from addons.Animation_addon.config import __addon_name__
from addons.Animation_addon.operators.AddonOperators import AnimationOperator, Animation2Operator
from common.i18n.i18n import i18n


class ExampleAddonPanel(bpy.types.Panel):
    bl_label = "Animation Addon Side Bar Panel"
    bl_idname = "SCENE_PT_AnimationAddonPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    # name of the side panel
    bl_category = "AnimationAddon"

    def draw(self, context: bpy.types.Context):
        addon_prefs = context.preferences.addons[__addon_name__].preferences

        layout = self.layout
        layout.operator(AnimationOperator.bl_idname)
        layout.operator(Animation2Operator.bl_idname)

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None
