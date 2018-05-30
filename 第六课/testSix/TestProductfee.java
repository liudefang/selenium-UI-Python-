package cn.TestScripts;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.Test;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

/**
 * Created by mike.liu on 2017/9/4.
 */
public class TestProductfee {
    static WebDriver driver;
    static String baseUrl;
    static Actions action;


    @Test(priority = 1)
    public void setUp() throws Exception {
        baseUrl = "http://10.1.2.211:8080/login.jsp";
        // 设定连接chrome浏览器驱动程序所在的磁盘位置，并添加为系统属性值
        System.setProperty( "webdriver.chrome.driver", "D:\\workspace\\ERP-KeyWordsFramework\\driver\\chromedriver.exe" );
        driver = new ChromeDriver();
        action = new Actions( driver );
    }

    @Test(priority = 2)
    public void FpLogin() throws Exception {
        driver.get( baseUrl + "" );

        driver.manage().window().maximize();

        // 文本框内输入用户名
        driver.findElement( By.name( "username" ) ).sendKeys( "defang3" );
        // 文本框内输入密码
        driver.findElement( By.name( "password" ) ).sendKeys( "123" );
        // 点击登录
        driver.findElement( By.className( "submit_wrap" ) ).click();

        Thread.sleep( 3000 );
        Thread.sleep( 3000 );
        // 点击产品中心链接
        driver.findElement( By.xpath( "//*[@id='10000013510266']" ) ).click();
        // 点击私募产品菜单
        Thread.sleep( 3000 );
        driver.findElement( By.xpath( "//*[@name='私募产品']" ) ).click();

        Thread.sleep( 2000 );

        WebElement currentTabIframe1 = findCurrentTabframe();

        if (currentTabIframe1 != null) {
            System.out.println( currentTabIframe1 );
            driver.switchTo().frame( currentTabIframe1 );
        }

        driver.findElement( By.xpath( "//input[@*='Q_crmCode_SL']" ) ).sendKeys( "D20161230485" );
        // driver.findElement(By.xpath("//input[@*='Q_crmCode_SL']")).sendKeys(contractCode);
        // 点击查找按钮
        driver.findElement( By.xpath( "//*[@id='btnSearch']" ) ).click();

        // 点击产品的明细按钮
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[text()='明细']" ) ).click();
        Thread.sleep( 2000 );


       // ((JavascriptExecutor) driver).executeScript( "window.scrollTo(0,document.body.scrollHeight)" );

       /* //点击下载按钮
        WebElement element = driver.findElement( By.xpath( "//*[text()='下载']" ) );

        //使用JavaScript的scrollIntoView()函数将滚动条滚动到页面的指定元素位置
        ((JavascriptExecutor) driver).executeScript( "arguments[0].scrollIntoView();",element );*/


        //使用JavaScript的scrollto函数，使用0和800的横纵坐标参数，将页面的滚动条纵向下滑800个像素
        ((JavascriptExecutor) driver).executeScript( "window.scrollBy(0,800)" );

        //点击添加费率按钮
        /*driver.findElement( By.xpath( "//*[@id='addFee']" ) ).click();


        Thread.sleep( 5000 );


        //输入协议主体机构
        driver.findElement( By.xpath( "//*[@id='agreementOrgId']" ) ).clear();
        driver.findElement( By.xpath( "//*[@id='agreementOrgId']" ) ).sendKeys( "夏道山测试数据" );

        //选择协议类型
       WebElement agreementType=driver.findElement( By.xpath( "//*[@id='agreementType']" ) );
        agreementType.findElement( By.xpath( "//option[@value='1']" ) ).click();

        // 创建一个dataformat对象
        SimpleDateFormat dataFormat = new SimpleDateFormat("yyyy-MM-dd");

        // 利用Date()获取当前时间
        Date date = new Date();
        // 格式化时间,并用String对象存储
        String date1 = dataFormat.format(date);
        Calendar ca = Calendar.getInstance();
        ca.add(Calendar.DATE, 10);// 当前日期加10天
        date = ca.getTime();
        String date2 = dataFormat.format(date) ;
        System.out.println(date1);
        System.out.println(date2);

        Thread.sleep(2000);
        driver.findElement(By.xpath("//*[@id='validityFrom']")).sendKeys(date1);
        driver.findElement(By.xpath("//*[@id='validityTo']")).sendKeys(date2);

        driver.findElement(By.xpath("//*[@name='InsRatioDate']")).sendKeys(date2);

        //点击保存按钮
        driver.findElement( By.xpath( "//*[@id='save-btn']" ) ).click();

        Thread.sleep( 3000 );
        //Assert.assertTrue( getClass().equals( "保存成功" ) );
        //点击保存成功的确定提示信息
        driver.findElement( By.xpath( "//*[@class='btn btn-primary modal-confirm']" ) ).click();

        Thread.sleep( 3000 );
        //添加认购费
        driver.findElement( By.xpath( "//*[@id='subscribeFeeBtn']" ) ).click();
        
		//输入第一阶梯收费的认购费率
        driver.findElement( By.xpath( "//*[@id='subscribe-form']/div[1]/div[2]/input[@name='applyFeePer']" ) ).sendKeys( "9" );
		//输入第一阶梯收费的百分比
        driver.findElement( By.xpath( "//*[@id='subscribe-form']/div[1]/div[3]/input[@name='dividePro']" ) ).sendKeys( "90" );
		//输入第二阶梯收费的认购金额
		driver.findElement( By.xpath( "//*[@id='subscribe-form']/div[2]/div[1]/div[1]/input[@*='applyFeeFrom']" ) ).clear();
        driver.findElement( By.xpath( "//*[@id='subscribe-form']/div[2]/div[1]/div[1]/input[@*='applyFeeFrom']" ) ).sendKeys( "500" );
		//输入第二阶梯收费的认购费率
        driver.findElement( By.xpath( "//*[@id='subscribe-form']/div[2]/div[2]/input[@name='applyFeePer']" ) ).sendKeys( "8" );
		//输入第二阶梯收费的百分比
        driver.findElement( By.xpath( "//*[@id='subscribe-form']/div[2]/div[3]/input[@name='dividePro']" ) ).sendKeys( "80" );

        Thread.sleep( 1000 );
        /*WebElement revenue=driver.findElement( By.xpath( "//*[@name='revenue']" ) );
        revenue.findElement( By.xpath( "//option[@value='1']" ) ).click();
        driver.findElement( By.xpath( "//input[@*='revenuePro']" ) ).sendKeys( "10" );*/
        //点击添加认购费的保存按钮
       /* driver.findElement( By.xpath( "//*[@class='btn btn-info save-subscribe save-subscribe-1']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@class='btn btn-primary modal-confirm']" ) ).click();
        //添加申购费
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@id='applyFeeBtn']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@id='applyFee-form']/div[1]/div[1]/div[2]/input[@name='applyFeeTo']" ) ).clear();
        driver.findElement( By.xpath( "//*[@id='applyFee-form']/div[1]/div[1]/div[2]/input[@name='applyFeeTo']" ) ).sendKeys( "500" );
        driver.findElement( By.xpath( "//*[@id='applyFee-form']//input[@*='applyFeePer']" ) ).sendKeys( "9" );
        driver.findElement( By.xpath( "//*[@id='applyFee-form']//input[@*='dividePro']" ) ).sendKeys( "90" );
        driver.findElement( By.xpath( "//*[@class='btn btn-info save-subscribe  save-subscribe-2']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@class='btn btn-primary modal-confirm']" ) ).click();

        //添加管理费
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@id='manageFeeBtn']" ) ).click();
        driver.findElement( By.xpath( "//input[@*='year']" ) ).sendKeys( "10" );
        driver.findElement( By.xpath( "//input[@*='manageFeeAfterDate']" ) ).sendKeys( date2 );
        driver.findElement( By.xpath( "//*[@id='manageFee-form']//input[@*='applyFeeTo']" ) ).clear();
        driver.findElement( By.xpath( "//*[@id='manageFee-form']//input[@*='applyFeeTo']" ) ).sendKeys( "500" );
        driver.findElement( By.xpath( "//*[@id='manageFee-form']//input[@*='applyFeePer']" ) ).sendKeys( "10" );
        driver.findElement( By.xpath( "//*[@id='manageFee-form']//input[@*='dividePro']" ) ).sendKeys( "90" );
        driver.findElement( By.xpath( "//*[@class='btn btn-info save-subscribe  save-subscribe-3']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@class='btn btn-primary modal-confirm']" ) ).click();
        //添加业绩报酬
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@id='performanceBtn']" ) ).click();
        driver.findElement( By.xpath( "//*[@id='performance-form']//input[@*='applyFeeTo']" ) ).clear();
        driver.findElement( By.xpath( "//*[@id='performance-form']//input[@*='applyFeeTo']" ) ).sendKeys( "500" );
        driver.findElement( By.xpath( "//*[@id='performance-form']//input[@*='applyFeePer']" ) ).sendKeys( "9" );
        driver.findElement( By.xpath( "//*[@id='performance-form']//input[@*='dividePro']" ) ).sendKeys( "90" );
        driver.findElement( By.xpath( "//*[@class='btn btn-info save-subscribe  save-subscribe-4']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@class='btn btn-primary modal-confirm']" ) ).click();
        //添加赎回费
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@id='redemptionFeeBtn']" ) ).click();
        driver.findElement( By.xpath( "//*[@id='redemption-form']//input[@*='applyFeeTo']" ) ).clear();
        driver.findElement( By.xpath( "//*[@id='redemption-form']//input[@*='applyFeeTo']" ) ).sendKeys( "500" );
        driver.findElement( By.xpath( "//*[@id='redemption-form']//input[@*='applyFeePer']" ) ).sendKeys( "9" );
        driver.findElement( By.xpath( "//*[@id='redemption-form']//input[@*='dividePro']" ) ).sendKeys( "90" );
        driver.findElement( By.xpath( "//*[@class='btn btn-info save-subscribe  save-subscribe-5']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@class='btn btn-primary modal-confirm']" ) ).click();
        //添加其它收入
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@id='otherFeeBtn']" ) ).click();
        driver.findElement( By.xpath( "//*[@id='otherFee-form']//input[@*='applyFeeTo']" ) ).clear();
        driver.findElement( By.xpath( "//*[@id='otherFee-form']//input[@*='applyFeeTo']" ) ).sendKeys( "500" );
        driver.findElement( By.xpath( "//*[@id='otherFee-form']//input[@*='applyFeePer']" ) ).sendKeys( "1000" );
        driver.findElement( By.xpath( "//input[@*='ps']" ) ).sendKeys( "测试的" );
        driver.findElement( By.xpath( "//*[@class='btn btn-info save-subscribe  save-subscribe-6']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[@class='btn btn-primary modal-confirm']" ) ).click();

        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[text()='返回']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[text()='提交审批']" ) ).click();
        Thread.sleep( 2000 );
        driver.findElement( By.xpath( "//*[text()='提交审批']" ) ).click();
        Thread.sleep( 2000 );
        //点击提交审批成功的确定按钮
        driver.findElement( By.xpath( "//*[@class='btn btn-primary modal-confirm']" ) ).click();*/



    }
    private WebElement findCurrentTabframe() {
        List<WebElement> eles = driver.findElements(By.tagName("iframe"));

        System.out.println(eles.size() + " ======");

        WebElement eleRet = null;

        for (WebElement ele : eles) {
            String src = ele.getAttribute("src");
            String id = ele.getAttribute("id");
            System.out.println("src: " + src + "id: " + id);

            if (src != null && src.contains("privateEquityProductInfo")) {
                eleRet = ele;
                break;
            }
        }

        return eleRet;
    }



}
