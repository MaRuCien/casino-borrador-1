import React, { useContext } from "react";
import { Context } from "../store/appContext";

const Menu = () => {
    const { store } = useContext(Context)
    return (
        <div className="container mt-5 mb-5">
            <h1>Menú de la semana</h1>
                <h6 className="mt-3 p-4 ml-5">Semana 19 al 22 de Julio 2022</h6>
                <div className="container">
                    <div className="row d-flex justify-content-center">
                        
                            {
                                !!store.menus &&
                                store.menus.map((menu) => {
                                    return(
                                        <div className="col-sm-12 col-lg-2 mb-4">
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
                                    )
                                })
                            }
                            <label className="mb-3 mt-4">
                                <input type="checkbox" name="check" value="si" autocomplete="off" /> Sí, quiero el almuerzo
                            </label>
                            <label className="mb-3">
                                <input type="checkbox" name="check" value="no" autocomplete="off" /> No, paso por hoy
                            </label>
                        </div>
            </div>
        </div>
    );
}

export default Menu; 