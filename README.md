I, `magichear`, made some adaptive modifications based on the [original code framework](https://github.com/KOHGYLW/kiftd-source?tab=readme-ov-file), as follows:

## commit record

- [v0.0.1] Finish initial work.

  - Add AutoRun.bat & ./RUN to auto run ai windows11.
  - Besides, change artifactId, version, name, url in pom.xml
  - **[CHEERS] Now we could use AutoRun.bat to build & run directly in windows11 !**

    - And we could also run at Linux just by simply change some places
    - [TODO:] This will be finished at next commit soon
      - Now is too late, I realy need a sleep

  - Adaptation for `windows`:
    - Automatically check the two folders `conf` and `filesystem` under the directory `C:\Users\Wanging\AppData\Local\Temp` at startup
      - Of course you should change `Wanging` to your own username
      - Even though these two folders might not be used, this ensures that the application can be used immediately without additional configuration
        - [TODO:] And I will find out what's happened and solve it
  - Modified `pom.xml`
    - Modified the `build` tag to include other resources to adapt to the `vsc` compilation scenario
    - `VSC` is the best IDE around the world!
  - And I add a file use_cloudflare_tunnel.py into ./RUN
    - With simply use this file, you could visit your web-program's port with a public address
    - But I'm not test it in win11 yet, only in Ubuntu22.04-destop
      - [TODO:] Maybe it will be finished at next commit or version

Below is the original `README`

## 欢迎访问 kiftd 源代码资源库！

### Welcome to visit source of kiftd!

_当前版本：v1.2.2-RELEASE_

### 简介

_kiftd——一款便捷、开源、功能完善的个人&团队&小型团队网盘服务器系统。_

---

## [![kiftd-mainpage.png](https://i.postimg.cc/gjyQRFVZ/kiftd-mainpage.png)](https://postimg.cc/dZ15PfSs)

kiftd 能够帮助您快速搭建起一个面向家庭、团队或组织的网盘系统，它操作简单、高效且功能多样。这里是 kiftd 的源代码资源库，您可以在这里获得 kiftd 的源代码，并对其进行下载、阅读与重构。

注：如果您仅仅希望得到一份拿来即用的软件，kiftd 也提供了一个完整的、解压即用的编译版。您可以根据其说明在 3 分钟内快速安装并开始使用。如果您需要该版本，请转到以下位置进行浏览和下载：
[kiftd-官方主页](https://kohgylw.github.io/)

### 构建说明

_下列条目为 kiftd 开发环境的基本信息，如需对源代码进行查看及编译，推荐使用所列配置。_

- JDK 版本：1.8.0
- 项目管理框架：Maven（m2e 1.8.0 for Eclipse）,Archetype：mavem-archetype-quickstart 1.1。
- 编码格式：UTF-8
- 项目资源及配置：Spring Boot+MyBatis+H2 DB，详见 pom.xml 文档。

### 快速开始

- 使用 Eclipse(javaEE)以项目方式导入本资源文件夹，并设置构建路径中的 JDK 版本。
- 使用 Maven 选项更新项目，并确保 pom 文件中引入的所有外部资源能够正确引入至本地。
- 打开 kohgylw.kiftd.mc.MC 类，进行测试运行。
- 右键项目，执行 Run with 选项中的 Maven install 操作以在 target 文件夹内编译生成 jar 程序。
- 将生成的 jar 程序拷贝到项目主目录下（即与 libs 等文件夹同级）并开始使用。

_提示：源代码路径下包含了一些程序运行所需的非源代码资源（例如程序图标等），某些集成式开发环境（例如 IDEA）在编译过程中可能会自动忽略非源代码资源。您需要设置并保证这些资源也能够被正确打包至最终的 jar 程序内，否则将会导致编译出的程序无法顺利运行。_

### 程序基本结构说明

- 源代码资源文件夹：/src/main/java/
- 入口类：kohgylw.kiftd.mc.MC
- web 界面请求处理包：kohgylw.kiftd.server.controller、kohgylw.kiftd.server.filter
- web 界面操作逻辑包：kohgylw.kiftd.server.service
- 核心功能及文件系统实现包：kohgylw.server.util、kohgylw.kiftd.server.listener、kohgylw.kiftd.server.mapper、kohgylw.kiftd.server.model
- 服务器行为控制类：kohgylw.server.ctl.KiftdCtl
- 服务器界面相关包：kohgylw.kiftd.ui、kohgylw.kiftd.printer
- 独立文件管理模块相关包：kohgylw.kiftd.util.file_system_manager
- 第三方工具使用许可证包：kohgylw.kiftd.util.licenses
- web 页面静态资源文件夹：/webContext/
- mybatis 映射表文件夹：/mybatisResource/
- 外部引用资源（编译后生成）文件夹：/libs/
- 引用字体文件夹：/fonts/
- 设置文件（程序第一次运行后生成）文件夹：/conf/
- 日志文件夹：/logs/
- 编译输出文件夹：/target/
- maven 配置文件：/pom.xml

### 常见问题&解决方案

- 使用 IDEA 导入项目后无法以图形界面方式运行

  > 在默认情况下，IDEA 可能会自动忽略位于项目源代码路径内的所有非源代码文件，从而导致图形界面需要的某些图标文件（例如 png 文件）无法被识别和打包。如遇此问题，请修改 IDEA 设置，确保项目源代码路径下的所有文件均会被识别和打包。

- 启动源代码项目时出现“Error creating bean with name org.mybatis.spring.mapper.MapperScannerConfigurer”
  > 如遇该问题，请尝试将 pom.xml 文件中引入的`mybatis`资源和`mybatis-spring`资源移除并重新添加`mybatis-spring-boot-starter`资源，从而避免默认整合方式可能导致的 Spring Boot 框架插件兼容性问题（特别鸣谢：用户 michael）。

### 使用许可（下载该源代码资源即视为接受以下许可）

当前版本的 kiftd 使用自带的许可文件进行分发。您应该先阅读该文件（获取方式：前往 kiftd 发行版主页下载一份 kiftd 发行版并在其中获得，详见 https://github.com/KOHGYLW/kiftd ），并在同意其中的所有条款后再下载该源代码。其大致内容如下：

- 您可以免费获得该源代码的原版拷贝。
- 您可以自由地对该源代码进行分发、重构并运用于任何领域。
- 作者对于使用该源代码造成的任何后果均无需负责。
- 作者对该源代码具有版权。

### 关于该源代码...

该源代码为目前发布的 kiftd 解压即用版的原始编译来源，二者保持一致性（有时源码版本可能会略微超前），作者将在今后对其逐步进行整理以便于用户阅读，由此带来的不便敬请谅解。

### 联系作者？

如有任何需要（例如对该资源有疑问、意见或建议），请发件联系作者： kohgylw@163.com （青阳龙野），随时恭候您的来信！

青阳龙野@kohgylw by 2024 年 07 月 20 日
