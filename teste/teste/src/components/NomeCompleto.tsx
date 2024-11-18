export function NomeCompleto({ nome }: any) {
  return (
    <p>
      {nome.firstName} {nome.lastName}
    </p>
  );
}
