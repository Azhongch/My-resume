import json
import sys
try:
    from jinja2 import Template
except ImportError:
    print("❌ 找不到 Jinja2 模組，請確認 build.yml 裡有安裝執行。")
    sys.exit(1)

def build_resume():
    try:
        # 讀取 JSON 資料
        with open('resume_data.json', 'r', encoding='utf-8') as f:
            resume_data = json.load(f)
        
        # 讀取 HTML 模板
        with open('template.html', 'r', encoding='utf-8') as f:
            template_str = f.read()
        
        # 使用 Jinja2 渲染
        template = Template(template_str)
        output_html = template.render(data=resume_data)
        
        # 輸出 index.html
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(output_html)
            
        print("✅ index.html 成功生成！")
        
    except Exception as e:
        print(f"❌ 執行發生錯誤：{e}")
        sys.exit(1)

if __name__ == "__main__":
    build_resume()
