import tailwindcss from "@tailwindcss/vite";
import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";
import { viteStaticCopy } from "vite-plugin-static-copy";

export default defineConfig({
  plugins: [
    sveltekit(),
    tailwindcss(),
    viteStaticCopy({
      targets: [
        {
          src: "src/routes/**/*.(png|webp)",
          dest: ".",
          rename: (fileName, fileExtension, fullPath) => {
            const relPath = fullPath.split(/src[\\\/]routes[\\\/]/)[1];
            const depth = relPath.split(/[\\\/]/).length + 1;
            return `${"../".repeat(depth)}${relPath}`;
          },
        },
      ],
      structured: true,
    }),
  ],
});
