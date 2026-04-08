print("Python is working")

try:
    print("\nTrying to import modules...")
    # 只导入模块，不执行代码
    import src.Work0.config
    import src.Work0.physics
    print("Successfully imported config and physics modules")
except Exception as e:
    print(f"Error importing modules: {e}")