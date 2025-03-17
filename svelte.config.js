import adapter from "@sveltejs/adapter-static";
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte";
import { mdsvex } from "mdsvex";
import rehypeAutolinkHeadings from "rehype-autolink-headings";
import rehypeSlug from "rehype-slug";

function get_headings() {
  let visit;
  let tree_to_string;
  let GithubSlugger;
  return async function transformer(tree, vFile) {
    if (!visit) {
      tree_to_string = (await import("mdast-util-to-string")).toString;
      visit = (await import("unist-util-visit")).visit;
      GithubSlugger = (await import("github-slugger")).default;
    }

    const slugger = new GithubSlugger();

    vFile.data.headings = [];

    visit(tree, "heading", (node) => {
      const title = tree_to_string(node);
      vFile.data.headings.push({
        level: node.depth,
        title,
        slug: slugger.slug(title),
      });
    });

    if (!vFile.data.fm) vFile.data.fm = {};
    vFile.data.fm.headings = vFile.data.headings;
  };
}

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Ensures both .svelte and .md files are treated as components (can be imported and used anywhere, or used as pages)
  extensions: [".svelte", ".svx"],

  // Consult https://svelte.dev/docs/kit/integrations
  // for more information about preprocessors
  preprocess: [
    vitePreprocess(),
    mdsvex({
      // Adds IDs to headings, and anchor links to those IDs. Note: must stay in this order to work.
      rehypePlugins: [
        rehypeSlug,
        [rehypeAutolinkHeadings, { behavior: "wrap" }],
      ],
      remarkPlugins: [get_headings],
    }),
  ],

  kit: {
    // adapter-auto only supports some environments, see https://svelte.dev/docs/kit/adapter-auto for a list.
    // If your environment is not supported, or you settled on a specific environment, switch out the adapter.
    // See https://svelte.dev/docs/kit/adapters for more information about adapters.
    adapter: adapter(),
  },
};

export default config;
