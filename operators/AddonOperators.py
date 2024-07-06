import time

import bpy
import math
from addons.Animation_addon.config import __addon_name__
from addons.Animation_addon.preference.AddonPreferences import ExampleAddonPreferences


# This Example Operator will scale up the selected object
class AnimationOperator(bpy.types.Operator):
    '''ExampleAddon'''
    bl_idname = "object.animation_ops"
    bl_label = "AnimationOperator"



    # 确保在操作之前备份数据，用户撤销操作时可以恢复
    bl_options = {'REGISTER', 'UNDO'}

    zoom: bpy.props.FloatProperty(name='Scale', default=1.0, min=0, max=10.0)
    zoom_collection: bpy.props.EnumProperty(items=[
        ('Scale', 'Scale', 'Scale the object'),
        ('Translate', 'Translate', 'Translate the object'),
        ('Rotate', 'Rotate', 'Rotate the object'),
    ], name='zoom_collection', default='Scale')

    # 操作的前提条件
    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):

        # for i in range(100):
        #     bpy.context.object.rotation_euler[2] += math.pi * 2  / 100
        #     bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        #     time.sleep(1 / 100)
        # bpy.context.object.scale *= self.Zoom * 2
        match self.zoom_collection:
            case 'Scale':
                context.active_object.scale *= self.zoom
            case 'Translate':
                context.active_object.location.z += self.zoom
            case 'Rotate':
                context.active_object.rotation_euler[2] += self.zoom
        return {'FINISHED'}

class Animation2Operator(bpy.types.Operator):
    '''ExampleAddon'''
    bl_idname = "object.animation2_ops"
    bl_label = "Animation2Operator"

    # 确保在操作之前备份数据，用户撤销操作时可以恢复
    bl_options = {'REGISTER', 'UNDO'}

    # 操作的前提条件
    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.active_object is not None

    def execute(self, context: bpy.types.Context):
        bpy.ops.object.animation_ops(zoom=10, zoom_collection='Rotate')
        return {'FINISHED'}