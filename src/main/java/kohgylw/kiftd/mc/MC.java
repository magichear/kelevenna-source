package kohgylw.kiftd.mc;
import java.io.File;
/**
 * 
 * <h2>kiftd主类（启动类）</h2>
 * <p>
 * 该类为程序主类，内部的main方法为kiftd程序的唯一入口。您可以从这里开始逐步了解kiftd的整个设计。
 * 如果需反馈问题，欢迎随时与作者联系：kohgylw@163.com，您的反馈将是kiftd不断完善的最佳动力。
 * </p>
 * <h4>许可声明：</h4>
 * <p>
 * 使用该源代码（包括但不限于：分发、修改、编译）代表您接受以下条款：
 * </p>
 * <ul>
 * <li>任何人均可以免费获取kiftd的源代码的原版拷贝，并进行分发或修改，并可用于任何用途。</li>
 * <li>经由该源代码或其修改版本编译而成的程序也可以运用于任何用途，无论是商业的还是非商业的。</li>
 * <li>作者青阳龙野（kohgylw@163.com）无需为使用该源代码或其编译生成的程序所导致的任何后果承担责任。</li>
 * <li>作者青阳龙野（kohgylw@163.com）保留kiftd原版源代码及其编译生成的程序的版权。</li>
 * 
 * 
 * <li>作者 magichear 基于原第一作者的代码框架进行了部分修改</li>
 * </ul>
 * 
 * @author 青阳龙野(kohgylw)
 * @author 第二作者 magichear
 * @version 1.0
 */



public class MC {
    public static void main(final String[] args) {
        // 调用创建目录的函数
        createDirectories();

        if (args == null || args.length == 0) {
            try {
                UIRunner.build(); // 以界面模式启动kiftd。
            } catch (Exception e) {
                // 提示：如果无法以图形界面启动，那么可能是由于资源引用失败或开发环境配置导致的，
                // 您可以根据此处捕获的异常对其进行调试。
                System.out.println(new String(
                        "错误！无法以图形界面模式启动kiftd，您的操作系统可能不支持图形界面。您可以尝试使用命令模式参数“-console”来启动并开始使用kiftd。".getBytes()));
            }
        } else {
            ConsoleRunner.build(args); // 以控制台模式启动kiftd。
        }
    }

    // 创建目录的函数
    private static void createDirectories() {
        String tempDir = System.getProperty("java.io.tmpdir");
        File confDir = new File(tempDir, "conf");
        File filesystemDir = new File(tempDir, "filesystem");

        if (!confDir.exists()) {
            confDir.mkdirs();
            System.out.println("已创建目录: " + confDir.getAbsolutePath());
        }

        if (!filesystemDir.exists()) {
            filesystemDir.mkdirs();
            System.out.println("已创建目录: " + filesystemDir.getAbsolutePath());
        }
    }
}
