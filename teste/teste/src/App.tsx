import Title from "./components/Title.tsx";
import Button from "./components/Button.tsx";
import "./app.css";
//import { HelloWorld } from "./components/HelloWorld.tsx";
import { NomeCompleto } from "./components/NomeCompleto.tsx";
import { Text } from "./components/Text.tsx";

export default function App() {
  return (
    <div>
      <Title />
      <Button />
      <NomeCompleto nome={{ firstName: "Bola", lastName: "MEN!" }} />
      <Text>{"XJIJFDJDGIDGIJ"}</Text>
      <Text>{"Morgs is at"}</Text>
    </div>
  );
}
