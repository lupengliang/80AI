### 了解需求
APP：
    支持移动设备 Android / iOS
    Mui + H5Plus
 
通讯服务：
    WebSocket(websocket握手原理 加密解密方式)
    通讯协议 - ? {sender:, receiver:, music/chat, sender_type}
    
逻辑服务：
    HTTP FlaskWeb框架
    1.足够轻量化
    2.快速的实现Http rest-API接口
    3.Flask 组件非常全
    
数据存储：
    MongoDB
    1.JSON存储 后期数据分析 用户画像
    2.数据格式不受限制
    3.存储读取速度很快
    
业务需求：
App需求：
    - 用户
        - 登录注册
        - 绑定玩具
    - 内容展示
        - 内容图片及音频
    - 聊天
        - 仿徽信通讯
    - 用户控制玩具通讯
    - 用户控制玩具播放内容
        - app websocket 实现内容推送
    
后台：
    FlaskWeb框架
    - 用户相关功能
        - 登录
        - 注册
        - 头像
        - 用户控制玩具
        
    - 文件功能相关
        - 文件内容传输
        - 文件上传？
    
    - 通讯服务：
        - 幼教内容推送到玩具
        - 可以和玩具进行通讯
        - 玩具和玩具进行通讯
        
采集内容 - 音频文件 - 喜马拉雅
