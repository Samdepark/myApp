import React from "react";

const CartItem = ({ item }) => {
  return (
    <div className="cart">
      <h2>This is a cart </h2>
      {/* <h3>{item.name}</h3>
      <p>Price: ${item.price}</p>
      <p>Quantity: {item.quantity}</p> */}
    </div>
  );
};

export default CartItem;
