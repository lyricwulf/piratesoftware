import "svelte/elements";

declare module "svelte/elements" {
  export interface DOMAttributes<T extends EventTarget> {
    "on:resetNav"?: (
      event: CustomEvent<{
        /* detail properties */
      }>
    ) => void;
  }
}
