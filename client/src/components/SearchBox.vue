<template>
    <div class="search-box">
        <div class="search-input">
            <input v-model="keywords" @keyup.enter="handleInputKeyDown" placeholder="Type to search...">
        </div>
        <div class="search-btn" @click="handleSearchClick">
            <i class="fas fa-search"></i>
        </div>
    </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
    data() {
        return {
            keywords: '',
            searchLink: 'https://www.bing.com/search?q='
        }
    },
    methods: {
        handleSearchClick() {
            if (this.keywords) {
                window.open(this.searchLink + encodeURI(this.keywords))
                this.keywords = ''
            }
        },
        handleInputKeyDown() {
            this.handleSearchClick()
        }
    }
})

</script>

<style lang="scss" scoped>
.search-box {
    display: flex;

    width: 400px;
    height: 40px;
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 20px;
}

.search-input {
    flex: 1;
    margin: 5px 5px 5px 10px;
}
.search-input input {
    margin: 0 20px;
    width: 100%;
    line-height: 30px;
    border: 0;
    outline: none;
    background: none;
}
.search-input input:focus::placeholder {
  color: transparent;
}

.search-btn {
    width: 40px;
    margin: 0 5px;

    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 18px;
    cursor: pointer;
    color: rgb(120, 120, 120);
}

@media (max-width: 820px) {
    .search-box {
        width: 60vw;
    }
}
@media (max-width: 600px) {
    .search-box {
        width: 70vw;
    }
}
</style>