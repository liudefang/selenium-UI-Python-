package cn.TestScripts;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class DdataProviderTest {

    private static WebDriver driver;
    @DataProvider(name = "user")
    public static Object[][] words()
    {
        return new Object[][] {
                {"defang1","123456","德芳理财"},
                {"defang2","123","德芳客服"},
                {"defang3","123","德芳运维"}
        };

    }
    @Test(dataProvider = "user")
    public void test(String user1,String user2,String SearchResult)
    {
        System.setProperty("webdriver.chrome.driver", "D:\\Selenium_Automated\\driver\\chromedriver.exe");
        driver = new ChromeDriver();
        //设定等待时间为10秒
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.get("http://10.1.2.211:8080/login.jsp");

        // 文本框内输入用户名
        driver.findElement( By.name( "username" ) ).sendKeys( user1 );
        // 文本框内输入密码
        driver.findElement( By.name( "password" ) ).sendKeys( user2 );
        // 点击登录
        driver.findElement( By.className( "submit_wrap" ) ).click();
        try {
            Thread.sleep(3000);

        } catch
                (InterruptedException e) {
            e.printStackTrace();
        }
        //判断搜索结果页面是否包含测试数据中期望的关键词
        Assert.assertTrue(driver.getPageSource().contains(SearchResult));
        driver.quit();

    }

}
