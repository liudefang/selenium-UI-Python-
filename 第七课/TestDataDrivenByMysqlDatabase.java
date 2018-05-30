package cn.TestScripts;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.io.IOException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class TestDataDrivenByMysqlDatabase {
    public WebDriver driver;
    String baseUrl = "http://10.1.2.211:8080/login.jsp";
    //使用注解DataProvider，将数据集合命名为“testData”
    @DataProvider(name = "testData")
    public static Object[][] words() throws IOException {
        //调用类中的静态方法getTestData，获取MySQL数据库中的测试数据
        return getTestData("testdata");

    }
    @Test(dataProvider = "testData")
    public void testSearch (String user1,String user2,String Result) {
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
    @BeforeMethod public void beforeMethod(){
        System.setProperty("webdriver.chrome.driver", "D:\\Selenium_Automated\\driver\\chromedriver.exe");
        driver = new  ChromeDriver();
    }
    @AfterMethod public void afterMethod(){
        driver.quit();
    }
    public static Object [][] getTestData(String tablename) throws IOException{
        //声明MySQL数据库的驱动
        String driver = "com.mysql.jdbc.Driver";
        //声明本地数据库的IP地址和数据库名称
        String url = "jdbc:mysql://10.1.2.71:3306/testdb";

        //声明数据库的用户名
        String user = "root";
        //声明数据库用户名的登录密码
        String password = "testjfz";
        //声明存储测试数据的list对象
        List<Object[] > records = new ArrayList<Object[] >();
        try {

            //设定驱动
            Class.forName(driver);
            //声明连接数据库的链接对象，使用数据库服务器地址，用户名和密码作为参数
            Connection conn = DriverManager.getConnection(url,user,password);
            //如果数据库链接可用，打印数据库连接成功的信息
            if(!conn.isClosed())
                System.out.println("连接数据库成功！");
            //创建statement对象
            Statement statement = conn.createStatement();
            //使用函数参数拼接要执行的sql语句，此语句用来获取数据表的所有数据行
            String sql = "SELECT * FROM " + tablename;
            //声明Resultset对象，存取执行sql语句返回的数据结果集
            ResultSet rs = statement.executeQuery(sql);
            //声明一个ResultSetMetadata对象
            ResultSetMetaData rsMetaData = rs.getMetaData();
            //调用ResultSetMetadata对象的getcolumncount方法获取数据行的列数
            int cols = rsMetaData.getColumnCount();
            //使用next方法遍历数据结构集中的所有数据行
            while (rs.next()) {
                //声明一个字符型数据，数组大小使用数据行的列个数进行声明
                String fields[] = new String[cols];
                int col = 0;
                //遍历所有数据行中的所有列数据，并存储在字符数组中
                for (int colIdx = 0; colIdx < cols; colIdx++) {
                    fields[col] = rs.getString(colIdx+1);
                    col++;
                }
                //将每一行的数据存储到字符数据后，存储到records中
                records.add(fields);
                //输出数据行中的前三列内容，用于验证数据库内容是否正确取出
                System.out.println(rs.getString(1) + " " + rs.getString(2) + " " + rs.getString(3));
            }
                //关闭数据结果集对象
                rs.close();
                //关闭数据库链接
                conn.close();
            } catch (ClassNotFoundException e){
                System.out.println("未能找到MySQL的驱动类！");
                e.printStackTrace();
            } catch(SQLException e){
                e.printStackTrace();
            } catch (Exception e){
                e.printStackTrace();
            }

            //定义函数返回值，即Object[][]
            //将存储测试数据的list转换成为一个object的二维数组
            Object[][] results = new Object[records.size()][];
            //设置二维数组每行的值，每行是一个Object对象
            for (int i = 0; i< records.size(); i++){
                results[i] = records.get(i);
            }
            return results;


    }
}


