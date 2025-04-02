import messages from "../messages.json";

export const MESSAGES_BY_ID = new Map<number, (typeof messages)[number]>();

messages.forEach((message) => {
  MESSAGES_BY_ID.set(message.id, message);
});
