# 🚀 HuggingFace Space 部署器

一个优雅的 Web 应用，让您能够一键将代码部署到 HuggingFace Spaces。

## ✨ 特性

- 🎯 **一键部署** - 简单几步即可部署您的应用
- 🎨 **优雅界面** - 使用 FastAPI + HTMX + DaisyUI + Tailwind CSS 构建
- 📊 **实时监控** - 实时查看部署进度和状态
- 🌙 **多主题** - 支持亮色、暗色和炫彩主题
- 📱 **响应式** - 完美适配各种设备
- 🔒 **安全可靠** - 使用您的 HuggingFace Token，数据安全

## 🛠️ 技术栈

- **后端**: FastAPI + Pydantic
- **前端**: HTMX + Jinja2 + DaisyUI + Tailwind CSS
- **部署**: HuggingFace Hub API
- **存储**: Redis (任务状态存储)

## 📦 安装

### 1. 克隆项目

```bash
git clone <repository-url>
cd huggingface-space-deployer
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 环境配置

创建 `.env` 文件：

```env
# API 密钥 (可选，用于 API 接口保护)
API_KEY=your_api_key_here

# Redis 配置 (可选，默认使用内存存储)
REDIS_URL=redis://localhost:6379
```

### 4. 启动应用

```bash
python main.py
```

应用将在 `http://localhost:8000` 启动。

## 🖥️ 使用方法

### Web 界面使用

1. 打开浏览器访问 `http://localhost:8000`
2. 填写部署表单：
   - **HuggingFace Token**: 在 [HuggingFace Settings](https://huggingface.co/settings/tokens) 创建具有写入权限的 Token
   - **Git 仓库 URL**: 您要部署的代码仓库地址
   - **Space 名称**: 在 HuggingFace 上的应用名称
   - **其他设置**: 描述、端口、环境变量等
3. 点击"开始部署"按钮
4. 实时查看部署进度
5. 部署成功后访问您的应用

### API 接口使用

#### 创建部署任务

```bash
curl -X POST "http://localhost:8000/deploy" \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "hf_token": "hf_...",
    "git_repo_url": "https://github.com/username/repo.git",
    "space_name": "my-app",
    "description": "My awesome app",
    "space_port": 7860,
    "private": false,
    "env_vars": {
      "API_KEY": "your_key"
    }
  }'
```

#### 查询部署状态

```bash
curl "http://localhost:8000/deploy/status/{task_id}" \
  -H "X-API-Key: your_api_key"
```

## 📋 部署要求

### 代码仓库要求

- 必须包含 `Dockerfile`
- Dockerfile 应该暴露指定端口
- 代码应该是可运行的容器化应用

### HuggingFace Token 要求

- Token 必须具有**写入权限**
- 在 [HuggingFace Settings](https://huggingface.co/settings/tokens) 创建

## 🚀 部署流程

1. **任务创建** - 生成唯一任务 ID
2. **代码克隆** - 从 Git 仓库克隆代码
3. **Space 创建** - 在 HuggingFace 创建新的 Space
4. **代码上传** - 将代码上传到 HuggingFace
5. **应用构建** - HuggingFace 自动构建 Docker 镜像
6. **应用部署** - 应用上线并可访问

## 🎨 界面特性

- **主题切换**: 支持亮色、暗色、炫彩三种主题
- **实时更新**: 使用 HTMX 实现无刷新状态更新
- **响应式设计**: 适配手机、平板、桌面设备
- **进度可视化**: 清晰的步骤指示器显示部署进度
- **错误提示**: 友好的错误信息和解决建议

## 🔧 配置说明

### 环境变量

| 变量名 | 描述 | 默认值 | 必需 |
|-------|------|--------|------|
| `API_KEY` | API 接口保护密钥 | - | 否 |
| `REDIS_URL` | Redis 连接 URL | 内存存储 | 否 |

### 应用配置

- **默认端口**: 7860 (Gradio/Streamlit 标准端口)
- **超时时间**: 15 分钟
- **支持框架**: 任何可容器化的 Web 应用

## 🐛 故障排除

### 常见问题

1. **部署失败: Token 无效**
   - 检查 HuggingFace Token 是否正确
   - 确保 Token 具有写入权限

2. **部署失败: 仓库克隆失败**
   - 检查 Git 仓库 URL 是否正确
   - 确保仓库可公开访问

3. **部署失败: 缺少 Dockerfile**
   - 在仓库根目录添加 Dockerfile
   - 确保 Dockerfile 语法正确

4. **应用构建失败**
   - 检查 Dockerfile 中的依赖
   - 确保应用代码可正常运行

### 日志查看

启动应用时会显示详细日志，包括：
- 请求处理日志
- 部署进度日志
- 错误详情日志

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

GPL-3.0 license

## 🔗 相关链接

- [HuggingFace Spaces](https://huggingface.co/spaces)
- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [HTMX 文档](https://htmx.org/)
- [DaisyUI 文档](https://daisyui.com/)

---

Made with ❤️ for the HuggingFace community
