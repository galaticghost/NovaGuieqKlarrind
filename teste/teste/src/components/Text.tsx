type TextProps = {
  children: string;
};
export function Text(props: TextProps) {
  return <p>{props.children}</p>;
}
