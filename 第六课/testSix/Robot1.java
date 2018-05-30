package cn.TestScripts;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import javax.security.auth.kerberos.KeyTab;
import java.awt.*;
import java.awt.datatransfer.StringSelection;
import java.awt.event.KeyEvent;

/**
 * Created by mike.liu on 2018/1/17.
 */
public class Robot1 {

    static WebDriver driver;
    static String baseUrl;
    static Actions action;



    @BeforeMethod
    public void beforeMethod() {

        baseUrl = "http://10.1.2.211:8080/login.jsp";
    }


    @Test(priority = 1)
    public void setUp() throws Exception {

        // 设定连接chrome浏览器驱动程序所在的磁盘位置，并添加为系统属性值
        //System.setProperty("webdriver.chrome.driver", ".\\driver\\geckodriver.exe");
        System.setProperty( "webdriver.chrome.driver","D:\\workspace\\ERP-KeyWordsFramework\\driver\\chromedriver.exe");
        driver = new ChromeDriver();
        action = new Actions(driver);
    }

    @Test(priority = 2)
    public void FpLogin() throws Exception {
        driver.get(baseUrl + "");

        driver.manage().window().maximize();

        WebDriverWait wait = new WebDriverWait( driver,10 );
        //使用显示等待，判断页面是否显示搜索框
        wait.until( ExpectedConditions.presenceOfElementLocated( By.name( "username"  ) ) );
      //调用封装好的函数setAndctrlVClipboardData，将“D20171228001”产品编码使用ctrl+v组合键方式粘贴到搜索框中
        setAndctrlVClipboardData("defang3");

        // 文本框内输入用户名
      //  driver.findElement( By.name( "username" ) ).sendKeys( "defang3" );
        // 文本框内输入密码
        driver.findElement( By.name( "password" ) ).sendKeys( "123" );
        // 点击登录
        //driver.findElement( By.className( "submit_wrap" ) ).click();

        //调用封装好的函数pressTabKey，按tab键，将焦点从搜索输入框转移到搜索按钮上
        pressTabKey();
        //调用封装好的函数pressEnterKey，按Enter键会触发搜索结果的提交
        pressEnterKey();

        Thread.sleep( 3000 );

    }
   /* @AfterMethod
    public void afterMethod(){
        driver.quit();
    }*/

    /*
    封装的粘贴函数，可以将函数的string参数值放入到剪贴板中，然后再使用Robot对象的KeyPress和keyRelease函数来模拟ctrl+v组合键完成粘贴操作
     */
    public void setAndctrlVClipboardData(String string){
        //声明StringSelection对象，并使用函数的string参数完成实例化
        StringSelection stringSelection = new StringSelection( string );
        //使用ToolKit对象的setContents方法将字符串放到剪切板中
        Toolkit.getDefaultToolkit().getSystemClipboard().setContents( stringSelection,null );
        //声明Robot对象
        Robot robot = null;
        try {
            //生成Robot的对象实例
            robot = new Robot();
        } catch (AWTException el) {
            el.printStackTrace();
        }
        //调用keyPress方法来实现按下Ctrl键
        robot.keyPress( KeyEvent.VK_CONTROL);
        //调用keyPress方法来实现按下V键
        robot.keyPress(KeyEvent.VK_V);
        //调用keyRelease方法来实现释放V键
        robot.keyRelease(KeyEvent.VK_V);
        //调用keyRelease方法来实现释放ctrl键
        robot.keyRelease(KeyEvent.VK_CONTROL);

    }



    public void pressTabKey(){
        Robot robot = null;
        try {
            robot = new Robot();

        } catch (AWTException e){
            e.printStackTrace();
        }
        //调用keyPress方法来实现按下tab键
        robot.keyPress(KeyEvent.VK_TAB);
        //调用keyRelease方法来实现释放Tab键
        robot.keyRelease(KeyEvent.VK_TAB);
    }

    public void pressEnterKey(){
        Robot robot = null;
        try {

            robot = new Robot();
        }catch (AWTException e){
            e.printStackTrace();
        }
        //调用keyPress方法来实现按下Enter键
        robot.keyPress(KeyEvent.VK_ENTER);
        //调用keyRelease方法来实现释放Enter键
        robot.keyRelease( KeyEvent.VK_ENTER);
    }
}
