namespace {{api}}
{


std::ostream & operator<<(std::ostream & stream, const {{identifier}} & value)
{
    stream << {{api}}binding::aux::Meta::getString(value);
    return stream;
}


} // namespace {{api}}