<template>
  <div class="planet">
    <div class="planet-container">
      <div class="planet-horizon">
        <img src="../assets/img/prince.png" alt="">
      </div>
      <continent
          :continent="continent"
          @landing="landedCon"
        />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { mapState, mapMutations } from 'vuex'
import Continent from './Continent.vue'

export default defineComponent({
  components: {
    Continent
  },
  computed: {
    ...mapState(['continent'])
  },
  methods: {
    ...mapMutations(['landedCon'])
  }
})
</script>

<style lang="scss">
.planet {
    width: 100vw;
    height: 100vh;
}
.planet-container {
    position: absolute;
    top: 80%;
    height: 100%;
    width: 100%;
}
.planet-horizon {
    height: 35px;
    width: 100%;
    background-color: rgba(255, 248, 231, 1);
    border-radius: 50% 50% 0 0 / 50% 50% 0 0;
    border: 0;
    margin-bottom: -6px;
}
.planet-horizon img {
  width: 35%;
  position: absolute;
  left: 60%;
  transform: translateY(-65%)
}
</style>
