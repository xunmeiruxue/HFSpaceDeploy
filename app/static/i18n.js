// Internationalization (i18n) support
const translations = {
    en: {
        // Navigation
        'nav.title': 'HF Space Deployer',
        'nav.theme': 'Toggle Theme',
        'nav.language': 'Language',
        
        // Hero Section
        'hero.title': 'One-Click Deploy',
        'hero.subtitle': 'Deploy to HuggingFace Spaces instantly',
        'hero.deployTime': 'Deploy Time',
        'hero.freeHosting': 'Free Hosting',
        'hero.minutes': '2-5min',
        'hero.percentage': '100%',
        
        // Features
        'feature.fast.title': 'Lightning Fast',
        'feature.fast.desc': 'Deploy from Git in minutes',
        'feature.secure.title': 'Secure',
        'feature.secure.desc': 'Full control with your token',
        'feature.monitor.title': 'Real-time',
        'feature.monitor.desc': 'Live deployment status',
        
        // Form
        'form.title': 'Configuration',
        'form.token': 'HuggingFace Token',
        'form.token.placeholder': 'hf_...',
        'form.token.get': 'Get Token',
        'form.token.hint': 'Write permission required',
        'form.repo': 'Git Repository',
        'form.repo.placeholder': 'https://github.com/user/repo.git',
        'form.repo.hint': 'GitHub, GitLab, etc.',
        'form.space': 'Space Name',
        'form.space.placeholder': 'my-app',
        'form.space.hint': 'Letters, numbers, hyphens only',
        'form.desc': 'Description',
        'form.desc.placeholder': 'Brief description...',
        'form.advanced': 'Advanced',
        'form.deployPath': 'Deploy Path',
        'form.deployPath.placeholder': '/',
        'form.deployPath.hint': 'Subdirectory to deploy (default: root)',
        'form.port': 'Port',
        'form.private': 'Private Space',
        'form.env': 'Environment Variables',
        'form.env.placeholder': 'KEY1=value\nKEY2=value',
        'form.env.hint': 'One per line',
        'form.submit': 'Deploy',
        
        // Requirements
        'req.title': 'Requirements',
        'req.dockerfile': 'Repository must contain Dockerfile',
        'req.token': 'Token needs write permissions',
        'req.time': 'Deployment takes 2-5 minutes',
        'req.docker': 'Supports Dockerized apps',
        
        // Pro Tips
        'tips.title': 'Tips',
        'tips.test': 'Test Dockerfile locally',
        'tips.env': 'Use env vars for secrets',
        'tips.size': 'Keep image size small',
        'tips.limits': 'Check HF resource limits',
        
        // Status Page
        'status.title': 'Deployment Status',
        'status.taskId': 'Task ID',
        'status.initializing': 'Initializing...',
        'status.preparing': 'Preparing your Space...',
        'status.queued': 'Queued',
        'status.queued.desc': 'Request received',
        'status.progress': 'In Progress',
        'status.progress.desc': 'Building and deploying...',
        'status.success': 'Success!',
        'status.success.desc': 'Your Space is live',
        'status.failed': 'Failed',
        'status.failed.desc': 'Deployment error',
        'status.url': 'Space URL',
        'status.visit': 'Visit Space',
        'status.error': 'Error Details',
        'status.troubleshoot': 'Troubleshooting',
        'status.newDeploy': 'New Deploy',
        'status.refresh': 'Refresh',
        'status.copy': 'Copy',
        'status.autoRefresh': 'Auto-refresh every 2s',
        
        // Loading
        'loading.title': 'Deploying...',
        'loading.desc': 'Please wait...',
        
        // Configuration Import/Export
        'config.import': 'Import',
        'config.export': 'Export',
        'config.import.title': 'Import Configuration',
        'config.import.info': 'Paste your configuration JSON or share configuration URL',
        'config.import.label': 'Configuration JSON',
        'config.import.placeholder': '{"space_name": "my-app", "git_repo_url": "https://github.com/..."}',
        'config.import.apply': 'Apply Configuration',
        'config.import.success': 'Configuration imported successfully',
        'config.import.error': 'Failed to import configuration',
        'config.import.empty': 'Please enter configuration JSON',
        'config.import.invalid': 'Invalid configuration format',
        'config.export.title': 'Export Configuration',
        'config.export.info': 'Configuration exported successfully',
        'config.export.label': 'Configuration JSON',
        'config.export.url': 'Share URL',
        'config.export.save': 'Save as File',
        'config.export.saved': 'Configuration saved to file',
        'config.copy': 'Copy',
        'config.copied': 'Configuration copied!',
        'config.url.copied': 'Share URL copied!',
        'config.cancel': 'Cancel',
        'config.close': 'Close',
        
        // Footer
        'footer.title': 'HF Space Deployer',
        'footer.desc': 'Quick deployment tool',
        
        // Copied toast
        'toast.copied': 'Copied!',
        'toast.copyFailed': 'Copy failed',
        'toast.deploySuccess': 'Deployment successful!',
        'toast.deployFailed': 'Deployment failed',
        'toast.requestFailed': 'Request failed'
    },
    
    zh: {
        // Navigation
        'nav.title': 'HF Space 部署器',
        'nav.theme': '切换主题',
        'nav.language': '语言',
        
        // Hero Section
        'hero.title': '一键部署',
        'hero.subtitle': '快速部署到 HuggingFace Spaces',
        'hero.deployTime': '部署时间',
        'hero.freeHosting': '免费托管',
        'hero.minutes': '2-5分钟',
        'hero.percentage': '100%',
        
        // Features
        'feature.fast.title': '极速部署',
        'feature.fast.desc': '分钟级 Git 部署',
        'feature.secure.title': '安全可靠',
        'feature.secure.desc': 'Token 完全掌控',
        'feature.monitor.title': '实时监控',
        'feature.monitor.desc': '部署状态实时更新',
        
        // Form
        'form.title': '配置设置',
        'form.token': 'HuggingFace 令牌',
        'form.token.placeholder': 'hf_...',
        'form.token.get': '获取令牌',
        'form.token.hint': '需要写入权限',
        'form.repo': 'Git 仓库',
        'form.repo.placeholder': 'https://github.com/用户名/仓库名.git',
        'form.repo.hint': '支持 GitHub、GitLab 等',
        'form.space': '空间名称',
        'form.space.placeholder': 'my-app',
        'form.space.hint': '仅限字母、数字、连字符',
        'form.desc': '描述',
        'form.desc.placeholder': '简短描述...',
        'form.advanced': '高级设置',
        'form.deployPath': '部署路径',
        'form.deployPath.placeholder': '/',
        'form.deployPath.hint': '要部署的子目录（默认：根目录）',
        'form.port': '端口',
        'form.private': '私有空间',
        'form.env': '环境变量',
        'form.env.placeholder': 'KEY1=value\nKEY2=value',
        'form.env.hint': '每行一个',
        'form.submit': '部署',
        
        // Requirements
        'req.title': '要求',
        'req.dockerfile': '仓库需包含 Dockerfile',
        'req.token': '令牌需要写入权限',
        'req.time': '部署需要 2-5 分钟',
        'req.docker': '支持 Docker 应用',
        
        // Pro Tips
        'tips.title': '提示',
        'tips.test': '先本地测试 Dockerfile',
        'tips.env': '敏感数据用环境变量',
        'tips.size': '保持镜像体积小',
        'tips.limits': '检查 HF 资源限制',
        
        // Status Page
        'status.title': '部署状态',
        'status.taskId': '任务 ID',
        'status.initializing': '初始化中...',
        'status.preparing': '准备 Space 中...',
        'status.queued': '排队中',
        'status.queued.desc': '已接收请求',
        'status.progress': '进行中',
        'status.progress.desc': '构建部署中...',
        'status.success': '成功！',
        'status.success.desc': 'Space 已上线',
        'status.failed': '失败',
        'status.failed.desc': '部署出错',
        'status.url': 'Space 地址',
        'status.visit': '访问 Space',
        'status.error': '错误详情',
        'status.troubleshoot': '故障排除',
        'status.newDeploy': '新建部署',
        'status.refresh': '刷新',
        'status.copy': '复制',
        'status.autoRefresh': '每2秒自动刷新',
        
        // Loading
        'loading.title': '部署中...',
        'loading.desc': '请稍候...',
        
        // Configuration Import/Export
        'config.import': '导入',
        'config.export': '导出',
        'config.import.title': '导入配置',
        'config.import.info': '粘贴配置 JSON 或分享配置链接',
        'config.import.label': '配置 JSON',
        'config.import.placeholder': '{"space_name": "my-app", "git_repo_url": "https://github.com/..."}',
        'config.import.apply': '应用配置',
        'config.import.success': '配置导入成功',
        'config.import.error': '配置导入失败',
        'config.import.empty': '请输入配置 JSON',
        'config.import.invalid': '配置格式无效',
        'config.export.title': '导出配置',
        'config.export.info': '配置导出成功',
        'config.export.label': '配置 JSON',
        'config.export.url': '分享链接',
        'config.export.save': '保存为文件',
        'config.export.saved': '配置已保存到文件',
        'config.copy': '复制',
        'config.copied': '配置已复制！',
        'config.url.copied': '分享链接已复制！',
        'config.cancel': '取消',
        'config.close': '关闭',
        
        // Footer
        'footer.title': 'HF Space 部署器',
        'footer.desc': '快速部署工具',
        
        // Copied toast
        'toast.copied': '已复制！',
        'toast.copyFailed': '复制失败',
        'toast.deploySuccess': '部署成功！',
        'toast.deployFailed': '部署失败',
        'toast.requestFailed': '请求失败'
    }
};

// Current language
let currentLang = localStorage.getItem('language') || 'en';

// Translate function
function t(key) {
    return translations[currentLang][key] || translations['en'][key] || key;
}

// Set language
function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('language', lang);
    updatePageTranslations();
}

// Toggle language
function toggleLanguage() {
    const newLang = currentLang === 'en' ? 'zh' : 'en';
    setLanguage(newLang);
}

// Update all translations on page
function updatePageTranslations() {
    // Update all elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        element.textContent = t(key);
    });
    
    // Update all elements with data-i18n-placeholder attribute
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        element.placeholder = t(key);
    });
    
    // Update all elements with data-i18n-title attribute
    document.querySelectorAll('[data-i18n-title]').forEach(element => {
        const key = element.getAttribute('data-i18n-title');
        element.title = t(key);
    });
    
    // Update document title
    document.title = t('nav.title');
    
    // Dispatch custom event
    document.dispatchEvent(new Event('languageChanged'));
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    updatePageTranslations();
}); 