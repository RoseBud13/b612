<template>
    <div id="toast" :class="[type]">
        {{ message }}
    </div>
</template>

<script>
export default {
  name: "Toast",
  props: {
    message: {
        type: String,
        default: ''
    },
    type: {
        type: String,
        default: 'success'
    }
  }
//   data() {
//     return {
//       message: "",//传递的消息
//       isActive: false,//是否处于活跃状态（显示在页面内）
//       type: "",//消息样式
//       timer1: null,
//       timer2: null,
//     };
//   },
//   mounted() {
//     this.$nextTick(() => {
//       this.isActive = true;
//     });
//     this.timer1 = setTimeout(() => {
//       this.isActive = false;
//     }, this.delayer);
//     this.timer2 = setTimeout(() => {
//       this.$destroy(true);//销毁vue实例
//     }, this.delayer * 2);
//   },
//   destroyed() {
//     this.$el.parentNode.removeChild(this.$el);//移除dom元素
//     clearTimeout(this.timer1);
//     clearTimeout(this.timer2);
//   },
};
</script>

<style scoped>
#toast {
    position: fixed;
    top: -50px;
    left: 50%;
    transform: translate(-50%, 0);
    padding: 13px 20px;
    border-radius: 15px;
    z-index: 999;
    opacity: 0;
    transition: all 1s;
}
#toast.success {
    top: 30px;
    opacity: 1;
    background-color: #f0f9eb;
    color: #67c23a;
}
#toast.error {
    top: 30px;
    opacity: 1;
    background-color: #fef0f0;
    color: #f56c6c;
}
#toast.warning {
    top: 30px;
    opacity: 1;
    background-color: #fefaf0;
    color: #f6a224;
}
/* #toast.active {
  top: 30px;
  opacity: 1;
} */
</style>