import React from "react";
import "../../../../node_modules/leaflet/dist/leaflet.css";
import { Link } from "react-router-dom";
import { TileLayer, MapContainer, Marker, Popup } from "react-leaflet";
import { Icon } from "leaflet";

const icon = new Icon ({
    iconUrl : '/location-sign.svg',
    iconSize : [25,25]
})


const Mapas = () => {



    return <MapContainer
    center={[-33.505, -70.70]}
    zoom={12}
    style={{width:'100vw', height:'100vh'}}>
       <TileLayer attribution= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
       url='https://tile.openstreetmap.org/{z}/{x}/{y}.png'/>

    <Marker 
    position={[-33.505, -70.70]}
    icon={icon}/>

    </MapContainer>
}


export default Mapas;