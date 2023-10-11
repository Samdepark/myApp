import React from 'react'
import '../Styles/Home.css'

function Home() {
 return (
    <div className="home">
      <div className="home__hero">
        <h1>Welcome to Our E-commerce Store</h1>
        <p>Discover the latest trends and products</p>
      </div>
      <div className="home__categories">
        <div className="home__category">
          <img src="https://via.placeholder.com/150" alt="Category 1" />
          <h2>Category 1</h2>
        </div>
        <div className="home__category">
          <img src="https://via.placeholder.com/150" alt="Category 2" />
          <h2>Category 2</h2>
        </div>
        <div className="home__category">
          <img src="https://via.placeholder.com/150" alt="Category 3" />
          <h2>Category 3</h2>
        </div>
      </div>
      <div className="home__products">
        <div className="home__product">
          <img src="https://via.placeholder.com/150" alt="Product 1" />
          <h2>Product 1</h2>
          <p>$99.99</p>
        </div>
        <div className="home__product">
          <img src="https://via.placeholder.com/150" alt="Product 2" />
          <h2>Product 2</h2>
          <p>$149.99</p>
        </div>
        <div className="home__product">
          <img src="https://via.placeholder.com/150" alt="Product 3" />
          <h2>Product 3</h2>
          <p>$199.99</p>
        </div>
      </div>
    </div>
 )
}

export default Home