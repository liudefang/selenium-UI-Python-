package cn.TestScripts;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.util.List;

/**
 * Created by mike.liu on 2018/1/17.
 */
public class Input_Experience {

    static WebDriver driver;
    static String baseUrl;
    static Actions action;


    @BeforeMethod
    public void beforeMethod() {

        baseUrl = "http://10.1.2.88:8080/login.jsp";
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
        driver.get( baseUrl + "" );

        driver.manage().window().maximize();

        // 文本框内输入用户名
        driver.findElement( By.name( "username" ) ).sendKeys( "defang1" );
        // 文本框内输入密码
        driver.findElement( By.name( "password" ) ).sendKeys( "123456" );
        // 点击登录
        driver.findElement( By.className( "submit_wrap" ) ).click();

        Thread.sleep( 3000 );
        // 点击交易中心链接
        driver.findElement( By.xpath( "//*[@id='70000000030487']" ) ).click();
        // 点击私募产品菜单
        Thread.sleep( 3000 );
        driver.findElement( By.xpath( "//*[@name='打款心得']" ) ).click();

        Thread.sleep( 3000 );
        driver.switchTo().frame( "iframe30000008531752" );
        //点击编辑按钮
        driver.findElement( By.xpath( "//*[text()='编辑']" ) ).click();

        Thread.sleep( 5000 );
        String body_string = "测试打款心得信息2";
        driver.switchTo().frame("ueditor_0");
        driver.findElement( By.tagName( "body" ) ).clear();
        driver.findElement( By.tagName( "body" ) ).sendKeys( body_string );
        driver.switchTo().parentFrame();


        Thread.sleep( 5000 );
        driver.findElement( By.xpath( "//*[text()='确定']" ) ).click();
       /* WebElement SaveBtn = SavePEBtn();

        if(SaveBtn != null)
        {
            SaveBtn.click();
        }*/


    }

    private static WebElement SavePEBtn() {

        //遍历选择双录弹出框，当找到保存按钮的时候，点击保存按钮
        List<WebElement> eles = driver.findElements( By.tagName("div"));

        System.out.println(eles.size() + "SavePEBtn ======");

        WebElement eleRet = null;

        for (WebElement ele : eles) {
            String id = ele.getAttribute("class");

            System.out.println("SavePEBtn class:"+ id);
            if (id.startsWith("l-dialog-btn-inner") && ele.getText().equals("保存")) {
                System.out.println(ele.getText());
                ele.click();
                break;
            }
        }
        return eleRet;
    }
}
