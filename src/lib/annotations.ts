const annotationFiles = Object.entries(
  import.meta.glob("/src/routes/**/annotation-*.svx", {
    eager: true,
  })
);

const ANNOTATIONS = new Map<number, any>();

for (const [filePath, fileModule] of annotationFiles) {
  const id = filePath.split("annotation-")[1].split(".")[0];
  ANNOTATIONS.set(Number(id), fileModule);
}

export default ANNOTATIONS;
