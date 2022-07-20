import { createApp } from 'vue'
import Toast from './Toast.vue'

const ToastPlugin = {};

function initToast(message, type, time) {
    return new Promise((res) => {
    
        // 组件实例第一个参数接收组，件第二个接收props
        const instance = createApp(Toast, {
            message: message || 'message',
            type: type || 'success'
        })
        
        // 组件容器
        const parentNode = document.createElement('div')
        document.body.appendChild(parentNode)
        instance.mount(parentNode)
        
        // 组件解绑
        function unmount() {
            instance.unmount()
            document.body.removeChild(parentNode)
        }
        
        // 解绑定时器
        setTimeout(() => {
            unmount()
            res()
        }, time)
    })
}

//使用app.use时候会自动调用install属性上的function
//参数中的Vue会自动传进来
//options是app.use的第二个参数
export default ToastPlugin.install = function (Vue, options) {
    let { name } = options
    //这里设定的属性在getCurrentInstance().proxy里面可以找到
    Vue.config.globalProperties[name] = initToast
}

// ToastPlugin.install = function (app) {
//   //1、实例化并绑定组件
//   const plugin = createApp(Toast);
//   const instance = plugin.mount(document.createElement("div"));

//   //2.将挂载的Node添加到body中
//   document.body.appendChild(instance.$el);

//   //3、定义全局
//   app.config.globalProperties.$toast = instance;
// };

// export default ToastPlugin;
