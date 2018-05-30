package cn.TestScripts;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.testng.annotations.Test;

import java.util.concurrent.TimeUnit;

/**
 * Created by mike.liu on 2017/7/20.
 */
public class OpenBrowserTest {
    static String  baseUrl ="http://10.1.2.211:8080/login.jsp";

    @Test
    public void FireFoxBrowser() {
        System.setProperty("webdriver.gecko.driver","E:\\Selenium for Java tools\\geckodriver.exe");

        System.setProperty("webdriver.firefox.bin", "D:\\Program Files\\Mozilla Firefox\\firefox.exe");
        //初始化一个火狐浏览器实例，实例名称叫drive
        WebDriver driver = new FirefoxDriver();
        //最大化窗口
        driver.manage().window().maximize();
        //设置隐性等待时间
        driver.manage().timeouts().implicitlyWait(8, TimeUnit.SECONDS);

        //get()打开一个站点
        driver.get(baseUrl);
        //getTitle()获取页面title的值
        System.out.print("当前打款页面的标题是：" + driver.getTitle());

        //关闭并退出浏览器
       // driver.quit();
    }

   /* @Test
    public void ChromeBrowser() {

        System.setProperty("webdriver.chrome.driver", ".\\driver\\chromedriver.exe");
        //初始化一个火狐浏览器实例，实例名称叫drive
        WebDriver driver = new ChromeDriver();
        //最大化窗口
        driver.manage().window().maximize();
        //设置隐性等待时间
        driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);

        //get()打开一个站点
        driver.get("https://www.icloud.com/");
        //getTitle()获取页面title的值
        System.out.print("当前打款页面的标题是：" + driver.getTitle());

        //关闭并退出浏览器
        //driver.quit();
    }
/*
    @Test
    public void IEBrowser() {

        System.setProperty("webdriver.chrome.driver", "D:\\workspace\\Selenium_Automated\\driver\\IEDriverServer.exe");
        //初始化一个火狐浏览器实例，实例名称叫drive
        WebDriver driver = new InternetExplorerDriver();
        //最大化窗口
        driver.manage().window().maximize();
        //设置隐性等待时间
        driver.manage().timeouts().implicitlyWait(8, TimeUnit.SECONDS);

        //get()打开一个站点
        driver.get(baseUrl);
        //getTitle()获取页面title的值
        System.out.print("当前打款页面的标题是：" + driver.getTitle());

        //关闭并退出浏览器
        driver.quit();
    }*/

}
