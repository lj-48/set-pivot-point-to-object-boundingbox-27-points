# -*- coding: GBK -*-
import maya.cmds as cmds
from functools import partial
import webbrowser


def get_two_point_center(position1, position2):
    return [
        (position1[0] + position2[0]) / 2,
        (position1[1] + position2[1]) / 2,
        (position1[2] + position2[2]) / 2
    ]


def setPivotsToBboxByXform(transform, pos):
    print pos
    cmds.xform(transform, piv=pos, ws=True)


def get_point(transform, num):
    bbox = cmds.exactWorldBoundingBox(transform)
    # Result: -0.5 -0.5 -0.5 0.5 0.5 0.5 #

    anchor_1 = [bbox[0], bbox[4], bbox[2]]
    anchor_2 = [bbox[3], bbox[4], bbox[2]]
    anchor_3 = [bbox[3], bbox[4], bbox[5]]
    anchor_4 = [bbox[0], bbox[4], bbox[5]]

    anchor_5 = [bbox[0], bbox[1], bbox[2]]
    anchor_6 = [bbox[3], bbox[1], bbox[2]]
    anchor_7 = [bbox[3], bbox[1], bbox[5]]
    anchor_8 = [bbox[0], bbox[1], bbox[5]]

    dic_ = {
        1: lambda: anchor_1,
        2: lambda: get_two_point_center(anchor_1, anchor_2),
        3: lambda: anchor_2,
        4: lambda: get_two_point_center(anchor_1, anchor_4),
        5: lambda: get_two_point_center(anchor_1, anchor_3),
        6: lambda: get_two_point_center(anchor_2, anchor_3),
        7: lambda: anchor_4,
        8: lambda: get_two_point_center(anchor_3, anchor_4),
        9: lambda: anchor_3,
        10: lambda: get_two_point_center(dic_[1](), dic_[19]()),
        11: lambda: get_two_point_center(dic_[2](), dic_[20]()),
        12: lambda: get_two_point_center(dic_[3](), dic_[21]()),
        13: lambda: get_two_point_center(dic_[4](), dic_[22]()),
        14: lambda: get_two_point_center(dic_[5](), dic_[23]()),
        15: lambda: get_two_point_center(dic_[6](), dic_[24]()),
        16: lambda: get_two_point_center(dic_[7](), dic_[25]()),
        17: lambda: get_two_point_center(dic_[8](), dic_[26]()),
        18: lambda: get_two_point_center(dic_[9](), dic_[27]()),
        19: lambda: anchor_5,
        20: lambda: get_two_point_center(anchor_5, anchor_6),
        21: lambda: anchor_6,
        22: lambda: get_two_point_center(anchor_5, anchor_8),
        23: lambda: get_two_point_center(anchor_5, anchor_7),
        24: lambda: get_two_point_center(anchor_6, anchor_7),
        25: lambda: anchor_8,
        26: lambda: get_two_point_center(anchor_7, anchor_8),
        27: lambda: anchor_7,

    }
    return dic_[num]()


def setPivotsToBbox(num, _):
    sels = cmds.ls(sl=True)
    if len(sels) != 1:
        cmds.error(u"至少选择一个模型")
    transform = sels[0]
    if cmds.nodeType(transform) != "transform":
        cmds.error(u"应该选择一个transform节点")
    point = get_point(transform, num)
    setPivotsToBboxByXform(transform, point)


def setPivotsToBboxUI_help():
    # if(cmds.window('setPivotsToBboxUI_help_ui',q=True,ex=True)):
    #     cmds.deleteUI('setPivotsToBboxUI_help_ui')
    # if (cmds.windowPref('setPivotsToBboxUI_help_ui', q=1, ex=1)):
    #     cmds.windowPref('setPivotsToBboxUI_help_ui', r=1)
    #
    # cmds.window('setPivotsToBboxUI_help_ui',t=u'help')
    # cmds.columnLayout('setPivotsToBboxUI_help_columnLayout_ui',adj=True)
    # cmds.scrollField(ww=True, text=u'从Y轴正方向往下看，Z轴正方向面向屏幕，呈现Z字形。这不同的27个按钮，分为上中下三层，每层每个点对应选择物体boundingbox的 顶点 或者 边的中心 或者 每一层的中心')
    # # cmds.text(h=20,align="left",wordWrap=True,width=100,hl=1,l=u'<a href=\"https://youtu.be/kqGpRak1PZE?list=PLAUgGUDpaMENfz8Nd7Zw-LxDK_v5ZflY6\"style=\"color:rgb(187,187,187)\;\">https://youtu.be/kqGpRak1PZE?list=PLAUgGUDpaMENfz8Nd7Zw-LxDK_v5ZflY6</a><br>')
    # cmds.iconTextbutton(l="1",l="视频教程",style="textOnly", bgc=(.2, .2, .2),c="shell start http://dennisporter3d.com/mel.htm")//不得行
    # cmds.showWindow('setPivotsToBboxUI_help_ui')

    webbrowser.open('https://www.baidu.com')


def ui():
    if (cmds.window('lj48_setPivotsToBbox', q=True, ex=True)):
        cmds.deleteUI('lj48_setPivotsToBbox')
    if (cmds.windowPref('lj48_setPivotsToBbox', q=1, ex=1)):
        cmds.windowPref('lj48_setPivotsToBbox', r=1)
    cmds.window('lj48_setPivotsToBbox', mb=True)
    cmds.menu('setPivotsToBboxUI_menu', l=u'help')
    cmds.menuItem('setPivotsToBboxUI_help', p='setPivotsToBboxUI_menu', l=u'help', c='setPivotsToBboxUI_help()')
    cmds.columnLayout('setPivotsToBboxUI_columnLayout_all', en=True, w=200, adj=False, cal=u'center', cw=200, rs=5)
    button_count = 1
    rowLayout_count = 1
    for i in range(1, 4):
        columnLayout_name = "setPivotsToBboxUI_columnLayout" + str(i)
        cmds.columnLayout(columnLayout_name, p="setPivotsToBboxUI_columnLayout_all", w=209, adj=True)
        for j in range(1, 4):
            rowLayout_name = "setPivotsToBboxUI_rowLayout" + str(rowLayout_count)
            cmds.rowLayout(rowLayout_name, p=columnLayout_name, w=200, nc=3)
            rowLayout_count += 1
            for k in range(1, 4):
                button_name = "setPivotsToBboxUI_button" + str(button_count)
                cmds.button(button_name, p=rowLayout_name, l=str(button_count), w=67, c=partial(setPivotsToBbox, button_count))
                button_count += 1

    cmds.showWindow('lj48_setPivotsToBbox')


ui()
