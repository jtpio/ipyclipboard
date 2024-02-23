function initialize({ model }) {
  window.addEventListener("copy", (event) => {
    const selection = window.getSelection();
    const text = selection.toString();
    model.set("value", text);
    model.save_changes();
  });

  model.on("change:value", () => {
    const value = model.get("value");
    void window.navigator.clipboard.writeText(value);
  });
}

function render( { model, el } ) {
  const value = model.get("value");
  el.innerHTML = `<pre>${value}</pre>`;
}

export default { initialize, render };
