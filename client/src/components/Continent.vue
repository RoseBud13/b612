<template>
  <div class="continent">
    <div class="continent_head">
      <div class="continent_icon">
        <i :class="['fa', `fa-${continent.icon}`]"></i>
      </div>
    </div>
    <div class="continent_body">
      <h3 class="continent_title">{{ continent.name }}</h3>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    continent: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      startY: 0, // 触摸位置
      endY: 0, // 结束位置
      disY: 0, // 移动距离
    }
  },
  mounted () {
    this.$el.addEventListener('touchstart', evt => {
      this.startY = evt.targetTouches[0].clientY;
    });
    this.$el.addEventListener('touchmove', evt => {
      this.endY = evt.targetTouches[0].clientY;
    });
    this.$el.addEventListener('touchend', () => {
      this.disY = this.endY - this.startY;

      if (this.startY != Math.abs(this.disY)) {
        //在滑动的距离超过屏幕高度的20%时，做某种操作
        // console.log('滑动',Math.abs(distanceY))
        if (Math.abs(this.disY) > 20) {
          // console.log(this.disY)
          //向下滑实行函数someAction1，向上滑实行函数someAction2
          if (this.disY < 0) {
              this.handleLanding()
          }
        }
      }
      this.startY = 0;
      this.endY = 0;
    });
  },
  methods: {
    handleLanding () {
      const appRect = document.querySelector('#app').getBoundingClientRect()
      const elRect = this.$el.getBoundingClientRect()
      const continent = this.continent
      const rect = {}
      rect.top = elRect.top - appRect.top
      rect.left = elRect.left - appRect.left
      rect.width = elRect.width
      rect.height = elRect.height
      rect.appWidth = appRect.width
      rect.appHeight = appRect.height
      this.$emit('landing', { rect, continent })
    }
  }
}
</script>

<style lang="scss">
.continent {
    background-color: rgba(255, 255, 255, 1);
    height: 100%;
    width: 100%;
    border: 0;
}
.continent_head {
  display: flex;
  padding: 20px;
  height: 44px;
  justify-content: space-between;
  align-items: flex-start;
  transform: translate3d(0, 0, 0);
  will-change: transform;
}
.continent_body {
  padding: 0 20px;
  transform: translate3d(0, 189px, 0);
  will-change: transform;
}
.continent_icon {
  display: flex;
  width: 44px;
  height: 44px;
  border: 1px solid #eee;
  border-radius: 100%;
  justify-content: center;
  align-items: center;
  font-size: 18px;
}
.continent_title {
  margin-top: 6px;
  font-size: 32px;
}
</style>
