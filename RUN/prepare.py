import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET


class AutoRun:
    def __init__(self):
        # 获取当前脚本所在目录
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # 获取父目录
        self.parent_dir = os.path.abspath(os.path.join(self.script_dir, os.pardir))

        # 拼接pom.xml文件路径
        self.pom_file = os.path.join(self.parent_dir, "pom.xml")

    def read_pom(self):
        # 解析pom.xml文件
        tree = ET.parse(self.pom_file)
        root = tree.getroot()

        # 定义命名空间
        namespaces = {"maven": "http://maven.apache.org/POM/4.0.0"}

        # 获取artifactId和version标签的内容
        artifact_id = root.find("maven:artifactId", namespaces).text
        version = root.find("maven:version", namespaces).text

        # 打印结果
        print(f"artifactId: {artifact_id}")
        print(f"version: {version}")

        # 拼接artifact_id和version为新的变量file
        file = f"{artifact_id}-{version}.jar"

        # 将file写入到filename.txt文件中
        filename_path = os.path.join(self.script_dir, "filename.txt")
        with open(filename_path, "w") as f:
            f.write(file)

        return file

    def build_and_copy_jar(self):
        # 获取jar文件名
        jar_file = self.read_pom()

        # 拼接jar文件路径
        jar_file_path = os.path.join(self.parent_dir, "target", jar_file)

        # 删除旧的 JAR 文件（实际上跟下面mvn clean 是重复的）
        if os.path.exists(jar_file_path):
            os.remove(jar_file_path)
            print(f"已删除旧的 JAR 文件: {jar_file_path}")

        # 使用 Maven 进行清理和编译
        os.chdir(self.parent_dir)
        try:
            # 编译
            os.system("mvn clean install")
            # 复制新的 JAR 文件到根目录
            destination_file_path = os.path.join(self.parent_dir, jar_file)
            shutil.copyfile(jar_file_path, destination_file_path)
            print(f"已复制新的 JAR 文件到根目录: {self.parent_dir}")
        except:
            print("编译失败，请检查错误信息。")
            sys.exit(1)


# 使用示例
if __name__ == "__main__":
    autorun = AutoRun()
    autorun.build_and_copy_jar()
