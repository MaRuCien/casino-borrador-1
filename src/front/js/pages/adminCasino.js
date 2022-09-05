import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

const AdminCasino = () => {

  const { store, actions } = useContext(Context);
  const [semana_id, setSemana_id] = useState(0);
  const [dia, setDia] = useState('');
  const [ensalada, setEnsalada] = useState('');
  const [principal, setPrincipal] = useState('');
  const [postre, setPostre] = useState('');
  const [bebida, setBebida] = useState('');
  const navigate = useNavigate();

  

  const menu = (event) => {
      event.preventDefault();
      actions.createMenu(semana_id, dia, ensalada, principal, postre, bebida);
      navigate('/menu-casino');
  };

  return (
    <form onSubmit={menu} className="container border border-5 border-success mt-5 shadow-lg p-3 mb-5 bg-white rounded" >
      <input 
      placeholder="Empresa"
      className="mt-3"
      type="text"
      name="empresa_id"
      value={semana_id}
      onChange={event => setSemana_id(event.target.value)}/>
      <input 
      placeholder="Día (de la semana)"
      className="mt-3"
      type="text"
      name="dia"
      value={dia}
      onChange={event => setDia(event.target.value)}/>
      <div className="row">
        <div className="col-xs-12 col-6">
          <div className="form-group mt-4 w-100">
            <label htmlFor="exampleFormControlTextarea1">Ensalada</label>
            <textarea
              className="form-control"
              id="exampleFormControlTextarea1"
              rows="3"
              value={ensalada}
              onChange={event => setEnsalada(event.target.value)}
            ></textarea>
          </div>
        </div>
        <div className="col-xs-12 col-6">
          <div className="form-group mt-4 w-100">
            <label htmlFor="exampleFormControlTextarea1">Principal</label>
            <textarea
              className="form-control"
              id="exampleFormControlTextarea1"
              rows="3"
              value={principal}
              onChange={event => setPrincipal(event.target.value)}
            ></textarea>
          </div>
        </div>
      </div>
      <div className="row mb-5">
        <div className="col-xs-12 col-6">
          <div className="form-group mt-4 w-100">
            <label htmlFor="exampleFormControlTextarea1">Postre</label>
            <textarea
              className="form-control"
              id="exampleFormControlTextarea1"
              rows="3"
              value={postre}
              onChange={event => setPostre(event.target.value)}
            ></textarea>
          </div>
        </div>
        <div className="col-xs-12 col-6">
          <div className="form-group mt-4 w-100">
            <label htmlFor="exampleFormControlTextarea1">Jugo / Otros</label>
            <textarea
              className="form-control"
              id="exampleFormControlTextarea1"
              rows="3"
              value={bebida}
              onChange={event => setBebida(event.target.value)}
            ></textarea>
          </div>
        </div>
      </div>
      <div className="d-flex justify-content-end">
        <button type="button" className="btn btn-success btn-lg m-2">
          Editar
        </button>
        <button type="submit" className="btn btn-success btn-lg m-2">
          Confirmar
        </button>
      </div>
    </form>
  );
};

export default AdminCasino;
