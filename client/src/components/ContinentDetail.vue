<template>
  <transition name="show" @enter="handleEnter" @leave="handleLeave">
    <div class="continent-detail" v-if="landed">
      <app-bar @left="departuredCon" />
      <continent :continent="landed.continent" />
    </div>
  </transition>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import AppBar from './AppBar.vue'
import Continent from './Continent.vue'
export default {
  components: {
    AppBar,
    Continent
  },
  computed: {
    ...mapState(['landed', 'departured'])
  },
  methods: {
    ...mapMutations(['departuredCon']),
    handleEnter (el) {
      Object.assign(el.style, {
        top: `${this.landed.rect.top}px`,
        left: `${this.landed.rect.left}px`,
        width: `${this.landed.rect.width}px`,
        height: `${this.landed.rect.height}px`
      })
      setTimeout(() => {
        Object.assign(el.style, {
          top: 0,
          left: 0,
          width: `${this.landed.rect.appWidth}px`,
          height: `${this.landed.rect.appHeight}px`
        })
      }, 0)
    },
    handleLeave (el) {
      Object.assign(el.style, {
        top: 0,
        left: 0,
        width: `${this.departured.rect.appWidth}px`,
        height: `${this.departured.rect.appHeight}px`
      })
      setTimeout(() => {
        Object.assign(el.style, {
          top: `${this.departured.rect.top}px`,
          left: `${this.departured.rect.left}px`,
          width: `${this.departured.rect.width}px`,
          height: `${this.departured.rect.height}px`
        })
      }, 0)
    }
  }
}
</script>

<style lang="scss">
.continent-detail {
  position: fixed;
  display: flex;
  flex-direction: column;
  border-radius: 0;
  background-color: white;
  color: #666;
  will-change: top, left, width, height;
  z-index: 9;

  .continent {
    margin: 0;
    margin-top: -44px;
    padding: 0 20px;
    box-shadow: none;
  }
  .continent_head,
  .continent_body {
    transform: translate3d(0, 88px, 0);
  }
  .app-bar {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
.show-enter-to,
.show-leave {
  border-radius: 0;

  .continent {
    padding: 0 20px;
  }
  .continent_head,
  .continent_body {
    transform: translate3d(0, 88px, 0);
  }
  .app-bar {
    opacity: 1;
    transform: translate3d(0, 0, 0);
  }
}
.show-leave-to,
.show-enter {
  border-radius: 8px;

  .continent {
    padding: 0;
  }
  .continent_head {
    transform: translate3d(0, 0, 0);
  }
  .continent_body {
    transform: translate3d(0, 189px, 0);
  }
  .app-bar {
    opacity: 0;
    transform: translate3d(0, -100%, 0);
  }
}
.show-enter-active,
.show-leave-active {
  transition: all 0.5s ease;

  .continent,
  .continent_head,
  .continent_body,
  .app-bar {
    transition: all 0.5s ease;
  }
}
</style>
