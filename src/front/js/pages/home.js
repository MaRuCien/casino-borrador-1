import React from "react";
import SlideCarousel from "../component/slideCarousel";
import TextoHome from "../component/textoHome";
import Registros from "../component/registro"

function Home() {
  return (
    <>
      <SlideCarousel />
      <TextoHome />
      <Registros />
    </>
  );
}

export default Home;
