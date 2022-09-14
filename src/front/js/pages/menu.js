import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { useState } from "react";

const Menu = () => {

  const { store, actions } = useContext(Context);

  const [check1, setCheck1] = React.useState(false);
  const [check2, setCheck2] = React.useState(false);
  const [userid, setUserid] = useState(0);

  const [decision1, setdecision1] = useState("Sí, quiero el almuerzo");
  const [decision2, setdecision2] = useState("No, paso por hoy");

  const checked1 = () => {
    setCheck1(!check1);
    setdecision1(decision1);
    console.log(decision1);
  };

  const checked2 = () => {
    setCheck2(!check2);
    setdecision2(decision2);
    console.log(decision2);
  };

  //test
  const decisionComidas = (event) => {
    event.preventDefault();
    if (check1 == true) decision = decision1;
    if (check2 == true) decision = decision2;

    console.log(decision);

    actions.decisionAlmuerzo(decision, userid);
    console.log(decision, userid);
  };

  var decision = "";

  return (
    <div className="container mt-5 mb-5">
      <h1>Menú de la semana</h1>
      <div className="border border-success border-5 mt-5">
        <h6 className="mt-3 p-4 ml-5">Semana 19 al 23 de Septiembre 2022</h6>
        <div className="container">
          <div className="row d-flex justify-content-center">
          {!!store.menus &&
            store.menus.map((menu, i) => {
              return (
                <div key={i} className="col-sm-12 col-lg-2 mb-4">
                  <div className="card">
                    <ul className="list-group list-group-flush">
                      <li className="dias list-group-item">{menu.dia}</li>
                      <li className="list-group-item">{menu.menus.ensalada}</li>
                      <li className="list-group-item">{menu.menus.principal}</li>
                      <li className="list-group-item">{menu.menus.postre}</li>
                      <li className="list-group-item">{menu.menus.bebida}</li>
                    </ul>
                  </div>
                </div>                             
                
              );
            })}
            <label className="mb-3 mt-4">
              <input
                type="checkbox"
                autocomplete="off"
                name="check1"
                value={check1}
                checked={check1}
                onChange={checked1}
              />{" "}
              {decision1}
            </label>
            <label className="mb-3">
              <input
                type="checkbox"
                autoComplete="off"
                name="check2"
                value={check2}
                checked={check2}
                onChange={checked2}
              />{" "}
              {decision2}
            </label>
          </div>
          <br />
          <p>
            Por favor selecciona tu numero de usuario entregado por tu empresa y
            selecciona solo uno de los campos:
          </p>
          <input
            placeholder="UserId"
            className="mt-3"
            type="text"
            name="userid"
            value={userid}
            onChange={(event) => setUserid(event.target.value)}
          />

          <button
            onClick={decisionComidas}
            type="button"
            className="btn btn-success w-100 mb-4"
          >
            Enviar
          </button>

        </div>
      </div>
    </div>
  );
};

export default Menu;
