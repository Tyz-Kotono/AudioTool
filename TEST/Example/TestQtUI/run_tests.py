import sys
import os
import subprocess

def clear_screen():
    """清除控制台屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """显示测试菜单"""
    clear_screen()
    print("=" * 40)
    print("     Qt UI 测试集合     ")
    print("=" * 40)
    print("请选择要运行的测试:")
    print("1. 基本 PySide6 测试 (test_pyside.py)")
    print("2. 基本 PyQt6 测试 (test_qt.py)")
    print("3. 主窗口测试 (main_pyside.py)")
    print("4. 简单可停靠窗口测试 (dock_test.py)")
    print("5. 高级可停靠窗口测试 (advanced_dock_test.py)")
    print("0. 退出")
    print("=" * 40)

def run_test(script_name):
    """运行指定的测试脚本"""
    print(f"正在运行 {script_name}...")
    try:
        subprocess.run([sys.executable, script_name], cwd=os.path.dirname(os.path.abspath(__file__)))
    except Exception as e:
        print(f"运行错误: {e}")
    input("\n按Enter键返回主菜单...")

def main():
    while True:
        show_menu()
        choice = input("请输入选项: ")
        
        if choice == '1':
            run_test("test_pyside.py")
        elif choice == '2':
            run_test("test_qt.py")
        elif choice == '3':
            run_test("main_pyside.py")
        elif choice == '4':
            run_test("dock_test.py")
        elif choice == '5':
            run_test("advanced_dock_test.py")
        elif choice == '0':
            print("退出程序...")
            break
        else:
            input("无效选项，按Enter键重试...")

if __name__ == "__main__":
    main() 