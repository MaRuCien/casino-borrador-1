import React, { useContext } from "react";
import { Context } from "../store/appContext";

const Menu = () => {
    const { store } = useContext(Context)
    return (
        <div className="container mt-5 mb-5">
            <h1>Menú de la semana</h1>
            <div className="border border-success border-5 mt-5">
                <h6 className="mt-3 p-4 ml-5">Semana 19 al 22 de Julio 2022</h6>
                <div className="container">
                    <div className="row d-flex justify-content-center">
                        
                            {
                                !!store.menus &&
                                store.menus.map((menu) => {
                                    return(
                                        <div className="col-sm-12 col-lg-2 border border-dark mb-4">
                                            
                                            <div className="container d-flex justify-content-between">
                                                <h3>{menu.dia}</h3>
                                            </div>
                                            <div className="container d-flex justify-content-between mt-4">
                                                <p><strong>Ensalada</strong></p>
                                            </div>
                                            <div className="container d-flex justify-content-between">
                                                <p>{menu.menus.ensalada}</p>
                                            </div>
                                            <div className="container d-flex justify-content-between mt-4">
                                                <p><strong>Plato principal</strong></p>
                                            </div>
                                            <div className="container d-flex justify-content-between">
                                                <p>{menu.menus.principal}</p>
                                            </div>
                                            <div className="container d-flex justify-content-between mt-4">
                                                <p><strong>Postre</strong></p>
                                            </div>
                                            <div className="container d-flex justify-content-between">
                                                <p>{menu.menus.postre}</p>
                                            </div>
                                            <div className="container d-flex justify-content-between mt-4">
                                                <p><strong>Jugo</strong></p>
                                            </div>
                                            <div className="container d-flex justify-content-between">
                                                <p>{menu.menus.bebida}</p>
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
        </div>
    );
}

export default Menu; 