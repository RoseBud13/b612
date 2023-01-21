<template>
    <div class="shelf-deck">
        <div class="shelf-view">
            <div class="shelf-items">
                <div class="shelf-upper">
                    <div class="book-item">
                        <img src="../../assets/img/book_cover.jpeg" alt="book">
                    </div>
                    <div class="book-item">
                        <img src="../../assets/img/book_cover.jpeg" alt="book">
                    </div>
                    <div class="book-item">
                        <img src="../../assets/img/book_cover.jpeg" alt="book">
                    </div>
                    <div class="book-item">
                        <img src="../../assets/img/book_cover.jpeg" alt="book">
                    </div>
                    <div class="book-item">
                        <img src="../../assets/img/book_cover.jpeg" alt="book">
                    </div>
                    <div class="book-item">
                        <img src="../../assets/img/book_cover.jpeg" alt="book">
                    </div>
                    <div class="book-item">
                        <img src="../../assets/img/book_cover.jpeg" alt="book">
                    </div>
                    <div class="book-item">
                        <img src="../../assets/img/book_cover.jpeg" alt="book">
                    </div>
                </div>
                <div class="shelf-lower">
                    <div class="film-item">
                        <img src="https://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                    </div>
                    <div class="film-item">
                        <img src="https://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                    </div>
                    <div class="film-item">
                        <img src="https://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                    </div>
                    <div class="film-item">
                        <img src="https://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                    </div>
                    <div class="film-item">
                        <img src="https://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                    </div>
                    <div class="film-item">
                        <img src="https://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                    </div>
                    <div class="film-item">
                        <img src="https://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                    </div>
                    <div class="film-item">
                        <img src="https://image.tmdb.org/t/p/w500//aKCvdFFF5n80P2VdS7d8YBwbCjh.jpg" alt="film">
                    </div>
                </div>
            </div>
            <div class="shelf-item-detail">
                <div class="item-wrapper">
                    <img src="../../assets/img/book_cover.jpeg" alt="book">
                    <div class="item-title">
                        <p>The Fault in Our Stars</p>
                    </div>
                    <div class="item-content">
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore vitae, iusto sed explicabo dolores consequatur pariatur, rerum tempora illo provident ad necessitatibus consectetur atque culpa itaque maxime delectus iste corrupti.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

</script>

<style lang="scss" scoped>
.shelf-deck {
    width: 100%;
    height: 100%;
}
.shelf-view {
    display: flex;
    // flex-direction: column;
    width: 100%;
    height: 100%;

    // * {
    //     border: 1px solid black;
    //     background-color: #eee;
    // }
}
.shelf-items {
    flex: 1;

    display: flex;
    flex-direction: column;
    max-width: calc(100% - 320px);
    height: 100%;
}
.shelf-item-detail {
    min-width: 320px;
    width: 320px;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.shelf-upper {
    flex: 1;

    display: flex;
    align-items: center;
    overflow-x: auto;
    height: 100%;
}
.shelf-upper::-webkit-scrollbar {
    display: none;
}
.book-item {
    height: 60%;
    aspect-ratio: 6 / 7;
    margin: 0 0 0 30px;
    background-color: rgba(137, 210, 235, 0.7);
    border-radius: 13%;

    display: flex;
    justify-content: center;
    align-items: center;
}
.book-item img {
    height: 70%;
    border-radius: 13%;
}
.shelf-lower {
    flex: 1;

    display: flex;
    align-items: center;
    overflow-x: auto;
    height: 100%;
}
.shelf-lower::-webkit-scrollbar {
    display: none;
}
.film-item {
    height: 60%;
    aspect-ratio: 6 / 7;
    margin: 0 0 0 30px;
    background-color: rgba(170, 235, 137, 0.7);
    border-radius: 13%;

    display: flex;
    justify-content: center;
    align-items: center;
}
.film-item img {
    height: 70%;
    border-radius: 13%;
}
.item-wrapper {
    height: 90%;
    width: 100%;
    background-color: rgba(137, 210, 235, 1);
    text-align: center;
    border-radius: 20px;
}
.item-wrapper img {
    height: 40%;
    margin: 10px;
}
.item-title {
    margin-top: 20px;
}
.item-title p {
    font-size: 1.1rem;
    color: #fff;
}
.item-content {
    margin: 20px 15px;
    padding: 10px;
    text-align: justify;
}
.item-content p {
    font-size: 0.9rem;
    color: #fff;
}

@media (max-width: 1440px) {
    .shelf-items {
        max-width: calc(100% - 280px);
    }
    .shelf-item-detail {
        min-width: 280px;
        width: 280px;
    }
    .item-wrapper img {
        height: 35%;
        margin: 10px;
    }
    .item-title {
        margin-top: 10px;
    }
}
</style>