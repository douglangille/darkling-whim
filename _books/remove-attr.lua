-- remove-attr.lua
function remove_attr (x)
  if x.attr then
    x.attr = pandoc.Attr()  -- drop id, classes, key/vals
  end
  return x
end

return {
  { Inline = remove_attr, Block = remove_attr }
}

