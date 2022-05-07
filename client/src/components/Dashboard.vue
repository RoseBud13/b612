<template>
    <div class="dashboard" :class="(showDashboard? 'show' : '')">
        <div class="dashboard-container">
            <div class="widget-box">
                <div class="daily-update"></div>
                <div class="widgets">
                    <div class="card">
                        <iframe src="https://rosebud13.github.io/bubble-player/" width="100%" height="200" style="border:none;"></iframe>
                    </div>
                    <div class="card img-card"></div>
                    <div class="mini-card"></div>
                    <div class="mini-card"></div>
                    <div class="card"></div>
                    <div class="mini-card"></div>
                </div>
            </div>
            <div class="app-box"></div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showDashboard: this.$store.state.showDashboard
        }
    },
    watch: {
        '$store.state.showDashboard'(newVal, oldVal) {
            this.showDashboard = newVal
            // console.log(this.showDashboard)
        },
    }
}
</script>

<style lang="scss">
.dashboard {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 0;

    z-index: 1;
    transition: all 1.2s ease-in-out;
}
.dashboard-container {
    width: 100%;
    height: calc(100% - 50px);
    color: rgb(255, 255, 255);
    margin-top: 50px;
    display: flex;

    // * {
    //     // border: 1px solid black;
    //     background-color: #eee;
    // }
}
.widget-box {
    width: 600px;
    
    display: flex;
    flex-direction: column;
}
.app-box {
    flex: 1;
}
.daily-update {
    background-color: white;
    height: 150px;
    margin: 15px 25px;
    border-radius: 30px;
}
.widgets {
    overflow: auto;

    padding-bottom: 20px;

    flex: 1;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.widgets::-webkit-scrollbar {
    display: none;
}
.card {
    background-color: rgba(255, 255, 255, 0.7);
    width: 550px;
    height: 200px;
    max-width: 550px;
    min-height: 200px;
    margin: 25px 25px 0 25px;
    border-radius: 30px;
}
.mini-card {
    background-color: rgba(255, 255, 255, 0.7);
    width: 250px;
    height: 250px;
    margin: 25px 25px 0 25px;
    border-radius: 30px;
}

.card iframe {
    border-radius: 30px;
}
.img-card {
    background-image: url(../assets/img/bili.webp);
    background-size: cover;
    background-position: center;
}

.show {
    height: 100%;
}

@media (max-width: 600px) {
    .dashboard-container {
        overflow: auto;
    }
    .widget-box {
        width: 100%;
    }
    .dashboard-container {
        flex-direction: column;
    }
    .widgets {
        flex-direction: column;
    }
    .card {
        width: auto;
    }
    .mini-card {
        width: auto;
    }
}
</style>
