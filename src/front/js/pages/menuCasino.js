import { format } from "prettier";
import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom"

const MenuCasino = () => {
  const { store } = useContext(Context);

  return (
    <div className="container">
      <div className="border border-5 border-success mt-5 mb-5 shadow-lg p-3 mb-5 bg-white rounded">
        <div className="row d-flex justify-content-center gx-0">
          {!!store.menus &&
            store.menus.map((menu, i) => {
              return (
                <div key={i} className="col-sm-12 col-lg-2 mb-4">
                  <div className="card">
                    <ul className="list-group list-group-flush">
                      <li className="list-group-item">{menu.dia}</li>
                      <li className="list-group-item">{menu.menus.ensalada}</li>
                      <li className="list-group-item">{menu.menus.principal}</li>
                      <li className="list-group-item">{menu.menus.postre}</li>
                      <li className="list-group-item">{menu.menus.bebida}</li>
                    </ul>
                  </div>
                </div>                             
                
              );
            })}
            <Link to="/admin-casino">
            <button  type="button" className="btn btn-success w-100 mb-4">
              Agregar
            </button>
            </Link>  
        </div>
      </div>
    </div>
  );
};

export default MenuCasino;
