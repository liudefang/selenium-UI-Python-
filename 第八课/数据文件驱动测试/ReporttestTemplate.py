# -*- encoding: utf-8 -*-


def htmlTemplate(trData):
    htmlStr = '''<!DOCTYPE HTML>
    <html>
    <head>
    <tittle>UI自动化测试报告</title>
    <style>
    body {
        width: 80%;  /*整个body区域占浏览器的宽度百分比*/
        margin: 40px auto;
        font-weight:bold;
        font-family:'trebuchet MS','Lucida sans',SimSun;
        font-size:18px;
        color:#000;
    }
    table {
         *border-coolapse:collapse; / *合并表格边框 */
         border-spacing:0; / *表格的边框宽度 */
         width:100%;     / *整个表格相对父元素的宽度 */
    }
    .tableStyle {
        /*border:solid #ggg 1px;*/
        border-style:outset;
        border-width:2px;
        /*border:2px;*/
        border-color:blue;
    }
    .tableStyle tr:hover {
        background:rgb(173,216,230);  /*鼠标滑过一行时，动态显示的颜色146,208,80*/
    }
    .tableStyle td,.tableStyle th{
        border-left:solid 1px rgb(146,208,80);
        border-top:1px solid rgb(146,208,80);
        padding:15px;
        text-align:center;
    }
    .tableStyle th{
        padding: 15px;
        background-color:rgb(146,208,80);
        background-image:-webkit-gradient(linear,left top,left bottom,from(#92D050), to(#A2D668));
        /*rgb(146,208,80)*/
    }
    </style>
    </head>
    <body>
         <center><h1>测试报告</h1></center><br />
         <table class= "tableStyle">
             <thead>
             <tr>
             <th>输入关键词</th>
             <th>预期结果</th>
             <th>开始时间</th>
             <th>耗 时</th>
             <th>Status</th>
             </tr>
             </thead>'''
    endStr = '''
        </table>
    </body>
    </html>'''
    # 拼接完整的测试报告HTML页面代码
    html = htmlStr + trData + endStr
    print(html)
    # 生成HTML文件
    with open(r"E:\\Python\\DataDrivenProject\\testTemplate.html", "w") as fp:
        fp.write(html)
