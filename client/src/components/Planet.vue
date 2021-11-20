<template>
  <div class="planet">
    <div class="planet-container">
      <div class="planet-horizon"></div>
      <continent
          :continent="continent"
          @landing="landedCon"
        />
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import Continent from './Continent.vue'

export default {
  components: {
    Continent
  },
  computed: {
    ...mapState(['continent'])
  },
  methods: {
    ...mapMutations(['landedCon'])
  }
}
</script>

<style lang="scss">
.planet {
    width: 100%;
}
.planet-container {
    position: absolute;
    top: 80%;
    height: 100vh;
    width: 100vw;
}
.planet-horizon {
    height: 35px;
    width: 100%;
    background-color: rgba(255, 255, 255, 1);
    border-radius: 50% 50% 0 0 / 50% 50% 0 0;
    border: 0;
    margin-bottom: -1px;
}
</style>
