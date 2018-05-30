package cn.TestScripts;

import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFCell;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class TestDataByExcelFile {

    private static WebDriver driver;
    String baseUrl = "http://10.1.2.211:8080/login.jsp";
    //使用注解DataProvider，将数据集合命名为“testData”
    @DataProvider(name="testData")
    public static Object[][] data() throws IOException
    {
        //调用类中的静态方法getTestData，获取Excel文件的测试数据
        return getTestData("D:\\Selenium_Automated\\testdata", "testdata.xlsx", "testdata");
    }
    @Test(dataProvider="testData")
    public void testSearch(String user1,String user2,String Result) {
        //打开erp首页
        driver.get(baseUrl);

        //使用数据库测试数据库表中每个数据行的前两列数据作为登录用户名和密码

        // 文本框内输入用户名
        driver.findElement(By.name("username")).sendKeys(user1);
        // 文本框内输入密码
        driver.findElement(By.name("password")).sendKeys(user2);
        // 点击登录
        driver.findElement(By.className("submit_wrap")).click();

        //判断搜索结果页面是否包含测试数据中期望的关键词
        Assert.assertTrue(driver.getPageSource().contains(Result));
    }
    @BeforeMethod
    public void beforeMethod() {

        System.setProperty("webdriver.chrome.driver", "D:\\Selenium_Automated\\driver\\chromedriver.exe");
        driver = new ChromeDriver();
        //设定等待时间为5秒
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
    }

    @AfterMethod
    public void afterMethod() {
        //关闭打开的浏览器
        driver.quit();
    }
    //从Excel文件获取测试数据的静态方法
    public static Object[][] getTestData(String filePath,String FileName,String sheetName) throws IOException{
        //根据参数传入的数据文件路径和文件名称，组合出Excel数据文件的绝对路径，声明一个File文件对象
        File file = new File(filePath + "\\" + FileName);
        //创建FileInputStream对象用于读取Excel文件
        FileInputStream inputStream = new FileInputStream(file);
        //声明workbook对象
        Workbook Workbook = null;
        //获取文件名参数的扩展名，判断是.xlsx文件还是.xls文件
        String fileExtensionName = FileName.substring(FileName.indexOf("."));
        //判断文件类型如果是.xlsx，则使用XSSFWORKbook对象进行实例化
        //判断文件类型如果是.xls，则使用ssfworkbook对象进行实例化
        if (fileExtensionName.equals(".xlsx")) {
            Workbook = new XSSFWorkbook(inputStream);
        } else if (fileExtensionName.equals(".xls")) {
            Workbook = new HSSFWorkbook(inputStream);
        }
        //通过sheetName参数，声称Sheet对象
        Sheet Sheet = Workbook.getSheet(sheetName);
        //获取Excel数据文件Sheet1中数据的行数，getLastRowNum()方法获取数据的最后一行行号
        //getFirstRowNum()方法获取数据的第一行行号，相减之后得出数据的行数，Excel文件的行号和列号都是从0开始
        int rowCount = Sheet.getLastRowNum() - Sheet.getFirstRowNum();
        //创建名为records的list对象来存储从Excel数据文件读取的数据
        List<Object[] > records = new ArrayList<Object[] >();
        //循环遍历Excel数据文件的所有数据，除了第一行，第一行是数据列名称
        for (int i = 1; i < rowCount + 1; i++) {
            //使用getShow方法获取行对象
            Row row = Sheet.getRow(i);
            //声明一个数组，存储Excel数据文件每行中的3个数据，数组的大小用getLastCellNum()方法进行动态声明，实现测试数据个数和数组大小一致
            String fields[] = new String[row.getLastCellNum()];
            for (int j = 0; j < row.getLastCellNum(); j++) {
                //使用getCell()和getStringCellValue()方法获取Excel文件中的单元格数据
                ////先设置getCell的类型，然后就可以把纯数字作为String类型读进来了：
                row.getCell(j).setCellType(Cell.CELL_TYPE_STRING);
                fields[j] = row.getCell(j).getStringCellValue();
                //函数返回指定单元格的字符串内容

            }
            //将fields的数据对象存入records的list中
            records.add(fields);
        }
        //定义返回值，即Object[][]
        // 将存储测试数据的List转换为一个Object的二维数组
        Object[][] results = new Object[records.size()][];
        // 设置二位数组每行的值，每行是一个Object对象
        for (int i = 0; i < records.size(); i++) {
            results[i] = records.get(i);
        }
        return results;
    }
}
