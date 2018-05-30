package cn.TestScripts;

import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxProfile;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class Downloader {
     WebDriver driver;

     String baseUrl;
    static Actions action;
    JavascriptExecutor js;

    public static String downloadFilePath = "D:\\downloadFiles";



    @BeforeMethod
    public void beforeMethod() {
        baseUrl = "http://10.1.2.211:8080/login.jsp";
    }



    @Test
    public void FpLogin() throws Exception {
        // 设定连接chrome浏览器驱动程序所在的磁盘位置，并添加为系统属性值
        // System.setProperty("webdriver.chrome.driver", "D:\\workspace\\Selenium_Automated\\driver\\geckodriver.exe");
        System.setProperty( "webdriver.firefox.bin", "D:\\Program Files\\Mozilla Firefox\\firefox.exe" );
        driver = new FirefoxDriver();

        driver.get( baseUrl );

        driver.manage().window().maximize();

        // 文本框内输入用户名
        driver.findElement( By.name( "username" ) ).sendKeys( "defang3" );
        // 文本框内输入密码
        driver.findElement( By.name( "password" ) ).sendKeys( "123" );
        // 点击登录
        driver.findElement( By.className( "submit_wrap" ) ).click();

        Thread.sleep( 3000 );
        // 点击产品中心链接
        driver.findElement( By.xpath( "//*[@id='10000013510266']" ) ).click();
        // 点击私募产品菜单
        Thread.sleep( 3000 );
        driver.findElement( By.xpath( "//*[@name='私募产品']" ) ).click();
        Thread.sleep( 3000 );
        //进入到ifram里面进行搜索
        driver.switchTo().frame( "iframe10000013510309" );
        driver.findElement( By.xpath( "//*[@name='Q_crmCode_SL']" ) ).sendKeys( "D20171228001" );


        Thread.sleep( 2000 );
        //点击查找按钮
        driver.findElement( By.xpath( "//*[@id='btnSearch']" ) ).click();
        // 点击产品的明细按钮
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[text()='明细']" ) ).click();
        Thread.sleep( 2000 );


        //点击下载按钮
        driver.findElement( By.xpath( "//*[text()='下载']" ) ).click();
        Thread.sleep( 5000 );
        try {
            Thread.sleep( 5000 );
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

        public static FirefoxProfile FirefoxDriverProfile() throws Exception{
        //声明一个profile对象
        FirefoxProfile profile = new FirefoxProfile();

        //设置Firefox的browser.download.folderList属性为2
        //如果 没有 进行 显示 设定， 则 使用 默认值 1， 表示 下载 文件 保存 在“ 下载” 文件夹
        // 设定 为 0， 则 下载 文件 会被 保存 在 用户 的 桌面 上
        // 设定 为 2， 则 下载 文件 会被 保存 在 指定 的 文件夹 下


        profile.setPreference("browser.download.folderList", 2);
        //browser. download. manager. showWhenStarting 的 属性 默认值 为 true
        // 设定 为 true， 则在 用户 启动 下载 的 时候 显示 Firefox 浏览器 的 文件 下载 窗口
        // 设定 为 false， 则在 用户 启动 下载 的 时候 不 显示 Firefox 浏览器 的 文件 下载 窗口

        profile.setPreference("browser.download.manager.showWhenStarting", false);
        //browser.download.dir设定下载文件保存的目录
        profile.setPreference("browser.download.dir", downloadFilePath);
        //browser.helperApps.neverAsk.openFile表示直接打开下载文件，不显示确认框
        //默认值为空字符串， 下行代码 行 设定 了 多种 文件 的 MIME 类型， 例如， application/ exe
        //表示． exe 类型 的 文件， application/ excel 表示 Excel 类型 的 文件
        profile.setPreference("browser.helperApps.neverAsk.openFile","application/octet-stream,application/exe,text/csv,application/pdf,application/x-msexcel,application/excel,application/x-excel,application/excel,application/x-excel,application/excel,application/vnd.ms-excel,application/x-excel,application/x-msexcel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml,application/excel");
        //browser. helperApps. neverAsk. saveToDisk 表示 下载 文件 是否 直接 保存 到 磁盘
        // 默认值 为 空 字符串， 下行 代码 行 设定 了 多种 文件 的 MIME 类型， 例如， application/ exe
        // 表示． exe 类型 的 文件， application/ excel 表示 Excel 类型 的 文件
        profile.setPreference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream,application/exe,text/csv,application/pdf,application/x-msexcel,application/excel,application/x-excel,application/excel,application/x-excel,application/excel,application/vnd.ms-excel,application/x-excel,application/x-msexcel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml,application/excel,text/x-c");

        // browser. helperApps. alwaysAsk. force 对于 未知 的 MIME 类型 文件 会 弹出 窗口
        // 让 用户 处理， 默认值 为 true， 设定 为 false 表示 不会 记录 打开 未知 MIME 类型 文件 的 方式
        profile.setPreference("browser.helperApps.alwaysAsk.force",false);
        //下载． exe 文件 弹出 警告， 默认值 是 true， 设定 为 false 则 不会 弹出 警告

        profile.setPreference("browser.download.manager.alertOnEXEOpen",false);
        // browser. download. manager. focusWhenStarting 设定 下载 框 在下 载 时会 获取 焦点

        // 默认值 为 true， 设定 为 false 表示 不 获取 焦点
        profile.setPreference("browser.download.manager.focusWhenStarting",false);
        // browser. download. manager. useWindow 设定 下载 是否 显示 下载 框， 默认值 为 true
        // 设定 为 false 会把 下载 框 进行 隐藏
        profile.setPreference("browser.download.manager.useWindow",false);
        // browser. download. manager. showAlertOnComplete 设定 下载 文件 结束 后 是否 显 示 下载  完成 提示 框，
        //框， 默认值 为 true， 设定 为 false 表示 下载 完成 后 不显 示 下载 完成 提示 框
        profile.setPreference("browser.download.manager.showAlertOnComplete",false);
        // browser. download. manager. closeWhenDone 设定 下载 结束 后 是否 自动 关闭 下载 框
        // 默认值 为 true， 设定 为 false 表示 不关 闭 下载 管理器
        profile.setPreference("browser.download.manager.closeWhenDone",false);
        return profile;
    }
}



















